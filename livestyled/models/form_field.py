from typing import Dict, List


class FormFieldTranslation:
    def __init__(
            self,
            id,
            language,
            label,
            placeholder,
            validation_error,
    ):
        self._id = id
        self.language = language
        self.label = label
        self.placeholder = placeholder
        self.validation_error = validation_error

    def __eq__(self, other):
        return all(
            [
                self.language == other.language,
                self.label == other.label,
                self.placeholder == other.placeholder,
                self.validation_error == other.validation_error
            ]
        )


class FormField:
    def __init__(
            self,
            id,
            type=None,
            key=None,
            required=None,
            translations=None,
            sort_id=None,
            validation_regex=None,
            select_options=None,
            auto_fill=None,
    ):
        self._id = id
        self.type = type
        self.key = key
        self.validation_regex = validation_regex
        self.required = required
        self.select_options = select_options
        self.sort_id = sort_id
        self.auto_fill = auto_fill
        self.translations = translations and [FormFieldTranslation(**translation) for translation in translations]

    @classmethod
    def create_new(
            cls,
            type: str or None = None,
            key: str or None = None,
            validation_regex: str or None = None,
            required: bool or None = None,
            sort_id: int or None = None,
            select_options: List or None = None,
            translations: List[FormFieldTranslation] or None = None,
            auto_fill: Dict or None = None,
    ):
        return FormField(
            id=None,
            type=type,
            key=key,
            validation_regex=validation_regex,
            required=required,
            select_options=select_options,
            sort_id=sort_id,
            translations=translations,
            auto_fill=auto_fill,
        )

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return '<FormField(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        fields = (
            'data', 'type', 'key', 'required', 'translations', 'sort_id', 'validation_regex', 'select_options', 'auto_fill'
        )
        return {field: getattr(self, field) for field in fields if getattr(self, field) != getattr(other, field)}

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            type=None,
            key=None,
            validation_regex=None,
            required=None,
            select_options=None,
            sort_id=None,
            translations=None,
            auto_fill=None,
        )
