from rest_framework.fields import HiddenField


class ParentHiddenRelatedField(HiddenField):
    """
    source: https://github.com/gretkierewicz/dissertation/blob/master/utils/relations.py

    Hidden Field that returns parent object pointed with URL
    or passed with serializer's data
    params: queryset - queryset to find parent's instance with
    params: parent_lookup_kwargs - parent's lookup URL kwargs names
    (keys) and fields (values)
    return: model instance
    """

    def __init__(self, queryset, parent_lookup_kwargs, **kwargs):
        self.queryset = queryset
        self.parent_lookup_kwargs = parent_lookup_kwargs
        kwargs["write_only"] = True
        kwargs["default"] = None
        super().__init__(**kwargs)

    def get_value(self, dictionary):
        # in case of bulk data sent, return instance hidden under
        # field's name. Instance needs to be set up in parent's
        # create/update methods
        if dictionary.get(self.field_name) and (
            dictionary.get(self.field_name) in self.queryset
        ):
            return dictionary.get(self.field_name)
        # update data forwarded to the to_internal_value() method
        filter_kwargs = {}
        for key, value in self.parent_lookup_kwargs.items():
            # get slug from URL resolver
            # needs to match parent_lookup_kwargs's names!
            if self.context.get("request"):
                filter_kwargs[value] = self.context.get(
                    "request"
                ).resolver_match.kwargs.get(key)
        return self.queryset.filter(**filter_kwargs).first()

    def to_internal_value(self, data):
        # return model's instance, no conversion needed
        return data
