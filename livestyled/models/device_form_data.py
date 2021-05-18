from livestyled.models.device import Device
from livestyled.models.form import Form


class DeviceFormData:
    def __init__(
            self,
            id,
            device_id,
            form_id,
            data,
            expires_at=None,
            created_at=None,
            updated_at=None
    ):
        self._id = id
        self.data = data
        self.created_at = created_at
        self.updated_at = updated_at
        self.expires_at = expires_at
        self._device = Device.placeholder(id=device_id)
        self._form = Form.placeholder(id=form_id)

    @classmethod
    def create_new(
            cls,
            device: Device or str or int,
            form: Form or str or int,
            data: list,
    ):
        device_form_data = DeviceFormData(
            id=None,
            device_id=None,
            form_id=None,
            data=data,
            expires_at=None,
            created_at=None,
            updated_at=None,
        )
        if isinstance(device, (str, int)):
            device = Device.placeholder(id=device)
        device_form_data._device = device
        if isinstance(form, (str, int)):
            form = Form.placeholder(id=form)
        device_form_data._form = form
        return device_form_data

    @property
    def id(self):
        return self._id

    @property
    def device_id(self):
        return self._device.id

    @property
    def device(self):
        return self._device

    @property
    def form_id(self):
        return self._form.id

    @property
    def form(self):
        return self._form

    def __repr__(self):
        return '<DeviceFormData(id={self.id!r}, device={self.device!r}, form={self.form!r})>'.format(self=self)

    def diff(self, other):
        fields = (
            'data',
        )
        return {field: getattr(self, field) for field in fields if getattr(self, field) != getattr(other, field)}
