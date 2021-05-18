from typing import List

from livestyled.models.form_field import FormField


class FormTranslation:
    def __init__(
            self,
            id,
            language,
            title,
            description,
            submit_button_title=None,
            completion_title=None,
            completion_button_title=None,
            completion_description=None,
    ):
        self._id = id
        self.language = language
        self.title = title
        self.description = description
        self.submit_button_title = submit_button_title
        self.completion_button_title = completion_button_title
        self.completion_title = completion_title
        self.completion_description = completion_description

    def __eq__(self, other):
        return all(
            [
                self.language == other.language,
                self.title == other.title,
                self.description == other.description,
                self.submit_button_title == other.submit_button_title,
                self.completion_title == other.completion_title,
                self.completion_button_title == other.completion_button_title,
                self.completion_description == other.completion_description
            ]
        )


class Form:
    def __init__(
            self,
            id,
            reference,
            image_url=None,
            completion_button_url=None,
            completion_button_title=None,
            show_completion_date=None,
            allow_update=None,
            refresh_on_success=None,
            fields=None,
            translations=None,
            requires_login=None,
            validation_integration=None,
    ):
        self._id = id
        self.reference = reference
        self.image_url = image_url
        self.completion_button_url = completion_button_url
        self.completion_button_title = completion_button_title
        self.show_completion_date = show_completion_date
        self.allow_update = allow_update
        self.refresh_on_success = refresh_on_success
        self.fields = fields and [FormField(**field) for field in fields]
        self.fields = translations and [FormTranslation(**translation) for translation in translations]
        self.requires_login = requires_login
        self.validation_integration = validation_integration

    @classmethod
    def create_new(
            cls,
            reference: str,
            image_url: str or None = None,
            completion_button_url: str or None = None,
            completion_button_title: str or None = None,
            show_completion_date: bool or None = None,
            allow_update: bool or None = None,
            refresh_on_success: bool or None = None,
            fields: List[FormField] or None = None,
            translations: List[FormTranslation] or None = None,
            requires_login: bool or None = None,
            validation_integration: str or None = None,
    ):
        return Form(
            id=None,
            reference=reference,
            image_url=image_url,
            completion_button_url=completion_button_url,
            completion_button_title=completion_button_title,
            show_completion_date=show_completion_date,
            allow_update=allow_update,
            refresh_on_success=refresh_on_success,
            fields=fields,
            translations=translations,
            requires_login=requires_login,
            validation_integration=validation_integration,
        )

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return '<Form(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        fields = (
            'data', 'reference', 'image_url', 'completion_button_url', 'completion_button_title', 'show_completion_date',
            'allow_update', 'refresh_on_success', 'fields', 'translations', 'requires_login', 'validation_integration'
        )
        return {field: getattr(self, field) for field in fields if getattr(self, field) != getattr(other, field)}

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            reference=None,
            image_url=None,
            completion_button_url=None,
            completion_button_title=None,
            show_completion_date=None,
            allow_update=None,
            refresh_on_success=None,
            fields=None,
            translations=None,
            requires_login=None,
            validation_integration=None,
        )
