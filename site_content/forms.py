from django import forms

from .models import Content

class HomePageContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ('homepage_title', 'homepage_first_img','homepage_title_description', 'homepage_content_description', 'homepage_content_img')

class ConceptContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ('concept_firstblock_title', 'concept_firstblock_content','concept_firstblock_background', 'concept_firstblock_img',
        'concept_secondblock_title', 'concept_secondblock_content', 'concept_thirdblock_title', 'concept_thirdblock_firstservice',
        'concept_thirdblock_secondservice', 'concept_thirdblock_thirdservice')