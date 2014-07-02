from django import forms

from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget


class TagForm(forms.ModelForm):
    tags = TagField(widget=LabelWidget)
