from django.test import TestCase, Client
from django.urls import reverse

from videos.views import index, viewvid
from main_app.models import Video

# Create your tests here.

class VideoAppTests(TestCase):
    def setUp(self):
        """
        Create a video for test database
        """
        Video.objects.create(
            title="Test Video 1", 
            link='https://youtu.be/4CI8Nt7y64s', 
            embed_link = 'https://www.youtube.com/embed/4CI8Nt7y64')

    def test_videos_index(self):
        """
        Is 'videos/index' valid?
        """
        client = Client()
        response = client.get(reverse('videos:index'))
        self.assertIs(response.status_code == 200, True)


    def test_specific_video(self):
        """
        Is videos/1 is valid?
        """
        client = Client()
        response = client.get(reverse('videos:viewvid', kwargs={'video_id':1}))
        self.assertIs(response.status_code == 200, True)





# test videos/# where # is an id (name videos/viewvid, context of a pk)