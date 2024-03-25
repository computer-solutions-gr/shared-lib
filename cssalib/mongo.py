from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from loguru import logger


class MongoDB:
    """
    MongoDB client class for connecting to a MongoDB database.

    Provides methods for pinging the server, listing databases and collections,
    and performing CRUD operations on collections. Designed to be instantiated
    with a MongoDB connection URI.
    """

    def __init__(self, uri):
        """
        Initializes a new MongoDB client using the provided URI.

        Args:
            uri (str): The URI for connecting to the MongoDB server.
        """

        # uri = "mongodb+srv://spitoglou:spitoglou@cluster0.kybxoii.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi("1"))

    def ping(self):
        """
        Pings the MongoDB deployment to check the connection status.
        """

        try:
            self.client.admin.command("ping")
            logger.debug(
                "Pinged your deployment. You successfully connected to MongoDB!"
            )
        except Exception as e:
            print(e)

    def list_databases(self):
        """
        Retrieves a list of database names from the MongoDB client.

        Returns:
            list: A list of database names.
        """

        db_names = self.client.list_database_names()
        logger.info(f"Found {len(db_names)} databases: {db_names}")
        return db_names

    def list_collections(self, database_name: str):
        """
        Retrieves a list of collection names for a specific database.

        Args:
            database_name (str): The name of the database to list collections from.

        Returns:
            list: A list of collection names in the specified database.
        """

        db = self.client[database_name]
        col_names = db.list_collection_names()
        logger.info(
            f"Found {len(col_names)} collections in {database_name}: {col_names}"
        )
        return col_names
