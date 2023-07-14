from sqlalchemy import Column, Integer, Text, String

from superagi.models.base_model import DBBaseModel


class VectordbConfigs(DBBaseModel):
    """
    Vector db related configurations like api_key, environment, and url are stored here
    Attributes:
        id (int): The unique identifier of the vector db configuration.
        vector_db_id (int): The identifier of the associated vector db.
        key (str): The key of the configuration setting.
        value (str): The value of the configuration setting.
    """

    __tablename__ = 'vector_db_configs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vector_db_id = Column(Integer)
    key = Column(String)
    value = Column(Text)

    def __repr__(self):
        """
        Returns a string representation of the Agent Configuration object.
        Returns:
            str: String representation of the Agent Configuration.
        """
        return f"VectorConfiguration(id={self.id}, key={self.key}, value={self.value})"
    
    @classmethod
    def get_vector_db_config_from_id(cls, session, vector_db_id):
        vector_db_configs = session.query(VectordbConfigs).filter(VectordbConfigs.vector_db_id == vector_db_id).all()
        config_data = {}
        for config in vector_db_configs:
            config_data[config.key] = vector_db_configs[config.value]
        return config_data