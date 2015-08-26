from ferris.tests.lib import WithTestBed
from app.models.post import Post


class TestPost(WithTestBed):

    def testQueries(self):
        # log in user one
        self.loginUser('user1@example.com')

        # create two posts
        post1 = Post(title="Post 1")
        post1.put()
        post2 = Post(title="Post 2")
        post2.put()

        # log in user two
        self.loginUser('user2@example.com')

        # create two more posts
        post3 = Post(title="Post 3")
        post3.put()
        post4 = Post(title="Post 4")
        post4.put()

        # Get all posts
        all_posts = list(Post.all_posts())

        # Make sure there are 4 posts in total
        assert len(all_posts) == 4

        # Make sure they're in the right order
        assert all_posts == [post4, post3, post2, post1]

        # Make sure we only get two for user2, and that they're the right posts
        user2_posts = list(Post.all_posts_by_user())

        assert len(user2_posts) == 2
        assert user2_posts == [post4, post3]

