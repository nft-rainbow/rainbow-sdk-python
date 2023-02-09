# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.gorm_deleted_at import GormDeletedAt
from openapi_server.models.models_exposed_metadata_attribute import ModelsExposedMetadataAttribute
from openapi_server import util


class ModelsExposedMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, animation_url: str=None, attributes: List[ModelsExposedMetadataAttribute]=None, created_at: str=None, deleted_at: GormDeletedAt=None, description: str=None, external_link: str=None, id: int=None, image: str=None, metadata_id: str=None, name: str=None, updated_at: str=None, uri: str=None):
        """ModelsExposedMetadata - a model defined in OpenAPI

        :param animation_url: The animation_url of this ModelsExposedMetadata.
        :param attributes: The attributes of this ModelsExposedMetadata.
        :param created_at: The created_at of this ModelsExposedMetadata.
        :param deleted_at: The deleted_at of this ModelsExposedMetadata.
        :param description: The description of this ModelsExposedMetadata.
        :param external_link: The external_link of this ModelsExposedMetadata.
        :param id: The id of this ModelsExposedMetadata.
        :param image: The image of this ModelsExposedMetadata.
        :param metadata_id: The metadata_id of this ModelsExposedMetadata.
        :param name: The name of this ModelsExposedMetadata.
        :param updated_at: The updated_at of this ModelsExposedMetadata.
        :param uri: The uri of this ModelsExposedMetadata.
        """
        self.openapi_types = {
            'animation_url': str,
            'attributes': List[ModelsExposedMetadataAttribute],
            'created_at': str,
            'deleted_at': GormDeletedAt,
            'description': str,
            'external_link': str,
            'id': int,
            'image': str,
            'metadata_id': str,
            'name': str,
            'updated_at': str,
            'uri': str
        }

        self.attribute_map = {
            'animation_url': 'animation_url',
            'attributes': 'attributes',
            'created_at': 'created_at',
            'deleted_at': 'deleted_at',
            'description': 'description',
            'external_link': 'external_link',
            'id': 'id',
            'image': 'image',
            'metadata_id': 'metadata_id',
            'name': 'name',
            'updated_at': 'updated_at',
            'uri': 'uri'
        }

        self._animation_url = animation_url
        self._attributes = attributes
        self._created_at = created_at
        self._deleted_at = deleted_at
        self._description = description
        self._external_link = external_link
        self._id = id
        self._image = image
        self._metadata_id = metadata_id
        self._name = name
        self._updated_at = updated_at
        self._uri = uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModelsExposedMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The models.ExposedMetadata of this ModelsExposedMetadata.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def animation_url(self):
        """Gets the animation_url of this ModelsExposedMetadata.


        :return: The animation_url of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._animation_url

    @animation_url.setter
    def animation_url(self, animation_url):
        """Sets the animation_url of this ModelsExposedMetadata.


        :param animation_url: The animation_url of this ModelsExposedMetadata.
        :type animation_url: str
        """

        self._animation_url = animation_url

    @property
    def attributes(self):
        """Gets the attributes of this ModelsExposedMetadata.


        :return: The attributes of this ModelsExposedMetadata.
        :rtype: List[ModelsExposedMetadataAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ModelsExposedMetadata.


        :param attributes: The attributes of this ModelsExposedMetadata.
        :type attributes: List[ModelsExposedMetadataAttribute]
        """

        self._attributes = attributes

    @property
    def created_at(self):
        """Gets the created_at of this ModelsExposedMetadata.


        :return: The created_at of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelsExposedMetadata.


        :param created_at: The created_at of this ModelsExposedMetadata.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ModelsExposedMetadata.


        :return: The deleted_at of this ModelsExposedMetadata.
        :rtype: GormDeletedAt
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ModelsExposedMetadata.


        :param deleted_at: The deleted_at of this ModelsExposedMetadata.
        :type deleted_at: GormDeletedAt
        """

        self._deleted_at = deleted_at

    @property
    def description(self):
        """Gets the description of this ModelsExposedMetadata.


        :return: The description of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelsExposedMetadata.


        :param description: The description of this ModelsExposedMetadata.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def external_link(self):
        """Gets the external_link of this ModelsExposedMetadata.


        :return: The external_link of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._external_link

    @external_link.setter
    def external_link(self, external_link):
        """Sets the external_link of this ModelsExposedMetadata.


        :param external_link: The external_link of this ModelsExposedMetadata.
        :type external_link: str
        """

        self._external_link = external_link

    @property
    def id(self):
        """Gets the id of this ModelsExposedMetadata.


        :return: The id of this ModelsExposedMetadata.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsExposedMetadata.


        :param id: The id of this ModelsExposedMetadata.
        :type id: int
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this ModelsExposedMetadata.


        :return: The image of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ModelsExposedMetadata.


        :param image: The image of this ModelsExposedMetadata.
        :type image: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")

        self._image = image

    @property
    def metadata_id(self):
        """Gets the metadata_id of this ModelsExposedMetadata.


        :return: The metadata_id of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, metadata_id):
        """Sets the metadata_id of this ModelsExposedMetadata.


        :param metadata_id: The metadata_id of this ModelsExposedMetadata.
        :type metadata_id: str
        """

        self._metadata_id = metadata_id

    @property
    def name(self):
        """Gets the name of this ModelsExposedMetadata.


        :return: The name of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsExposedMetadata.


        :param name: The name of this ModelsExposedMetadata.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelsExposedMetadata.


        :return: The updated_at of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelsExposedMetadata.


        :param updated_at: The updated_at of this ModelsExposedMetadata.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def uri(self):
        """Gets the uri of this ModelsExposedMetadata.


        :return: The uri of this ModelsExposedMetadata.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ModelsExposedMetadata.


        :param uri: The uri of this ModelsExposedMetadata.
        :type uri: str
        """

        self._uri = uri