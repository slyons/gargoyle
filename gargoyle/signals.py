from django.dispatch import receiver, Signal

switch_disabled = Signal(providing_args=["instance"])
switch_enabled = Signal(providing_args=["instance"])