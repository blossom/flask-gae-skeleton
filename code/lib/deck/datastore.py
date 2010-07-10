from google.appengine.ext import db
from google.appengine.api import datastore_types
from django.utils import simplejson

class JsonProperty(db.Property):
    """
    from appengine cookbook recipies
    http://appengine-cookbook.appspot.com/recipe/add-a-jsonproperty-to-your-model-to-save-a-dict-to-the-datastore/
    """
    def get_value_for_datastore(self, model_instance):
        value = super(JsonProperty, self).get_value_for_datastore(model_instance)
        return db.Text(self._deflate(value))
    def validate(self, value):
        return self._inflate(value)
    def make_value_from_datastore(self, value):
        return self._inflate(value)
    def _inflate(self, value):
        if value is None:
            return {}
        if isinstance(value, unicode) or isinstance(value, str):
            return simplejson.loads(value)
        return value
    def _deflate(self, value):
        return simplejson.dumps(value)
    data_type = datastore_types.Text
