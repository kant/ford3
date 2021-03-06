import json
from django.urls import reverse
from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories


class TestSaqaQualificationsView(TestCase):
    def setUp(self):
        self.saqa = ModelFactories.get_saqa_qualification_test_object()

    def test_search_by_saqa_id(self):
        query = 'q={}'.format(self.saqa.saqa_id)

        response = self.client.get(
            '{url}?{query}'.format(
                url=reverse('search-saqa-qualifications'),
                query=query))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 1)
        self.assertEqual(
            content['results'][0]['name'],
            self.saqa.name)

    def test_search_by_name(self):
        query = 'q={}'.format(self.saqa.name[0:8])

        response = self.client.get(
            '{url}?{query}'.format(
                url=reverse('search-saqa-qualifications'),
                query=query))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 1)
        self.assertEqual(
            content['results'][0]['name'],
            self.saqa.name)

    def test_search_by_name_case_insensitive_lower(self):
        query = 'q={}'.format(self.saqa.name[0:8].lower())

        response = self.client.get(
            '{url}?{query}'.format(
                url=reverse('search-saqa-qualifications'),
                query=query))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 1)
        self.assertEqual(
            content['results'][0]['name'],
            self.saqa.name)

    def test_search_by_name_case_insensitive_upper(self):
        query = 'q={}'.format(self.saqa.name[0:8].upper())

        response = self.client.get(
            '{url}?{query}'.format(
                url=reverse('search-saqa-qualifications'),
                query=query))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 1)
        self.assertEqual(
            content['results'][0]['name'],
            self.saqa.name)

    def test_search_empty_query(self):
        query = 'q='
        response = self.client.get(
            '{url}?{query}'.format(
                url=reverse('search-saqa-qualifications'),
                query=query))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 0)

    def test_search_without_query(self):

        response = self.client.get(
            '{url}'.format(
                url=reverse('search-saqa-qualifications')))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 0)

    def test_search_as_post(self):
        response = self.client.post(
            '{url}?'.format(
                url=reverse('search-saqa-qualifications')))

        content = json.loads(response.content)

        self.assertEqual(len(content['results']), 0)
