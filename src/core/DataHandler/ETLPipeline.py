import os
from dotenv import load_dotenv
import apache_beam as beam
from apache_beam.io.gcp.datastore.v1new.types import Query
from apache_beam.io import WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions
from typing import List, Dict

class DatastoreToBigQueryPipeline:
    """Class to store data from Datastore to BigQuery"""
    
    def __init__(self):
        """Load environment variables from .env file
        """
        # Loading environment variables from .env file
        load_dotenv()  
        self.project = os.getenv('GCP_PROJECT')
        self.namespace = os.getenv('DATASTORE_NAMESPACE')
        self.kind = os.getenv('DATASTORE_KIND')
        self.output_table = os.getenv('BIGQUERY_TABLE')
        self.staging_location = os.getenv('STAGING_LOCATION')
        self.temp_location = os.getenv('TEMP_LOCATION')

    def run_pipeline(self):
        """Run the pipeline to store data from Datastore to BigQuery"""
        
        options = PipelineOptions()
        google_cloud_options = options.view_as(GoogleCloudOptions)
        google_cloud_options.project = self.project
        google_cloud_options.job_name = 'datastore-to-bigquery'
        google_cloud_options.staging_location = self.staging_location
        google_cloud_options.temp_location = self.temp_location

        with beam.Pipeline(options=options) as p:
            # Read from Datastore
            datastore_query = Query(self.project, self.namespace, self.kind)
            datastore_data = p | 'ReadFromDatastore' >> beam.io.gcp.datastore.v1new.ReadFromDatastore(
                query=datastore_query)

            # Transform the data (will check later)
            # Transform the byte code into a string
            # transformed_data = datastore_data | 'TransformByteToString' >> beam.Map(
            #     self._transform_byte_to_string)


            # Write to BigQuery
            datastore_data | 'WriteToBigQuery' >> WriteToBigQuery(
                self.output_table,
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
            
    @staticmethod
    def _transform_byte_to_string(entity:str) -> List[str]:
        # Assuming 'byte_column' is the name of the column containing byte code
        byte_column = 'byte_column' # TODO: will change later

        # Decode the byte code into a string using an appropriate encoding (e.g., 'utf-8')
        entity[byte_column] = entity[byte_column].decode('utf-8')
        print(entity[byte_column])

        return entity


def main():
    # Create an instance of the DatastoreToBigQueryPipeline class
    pipeline = DatastoreToBigQueryPipeline()

    # Run the pipeline
    pipeline.run_pipeline()


if __name__ == '__main__':
    main()
