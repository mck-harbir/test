import datetime
import hashlib
from flask_login import UserMixin



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.Text())
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    followed = db.relationship('Followed', backref='follower', lazy='dynamic')
    followers = db.relationship('Followed', backref='following', lazy='dynamic')
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    library = db.relationship('Library', backref='owner', lazy='dynamic')


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = kwargs.get('password', None)


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    @password.setter
    def password(self, password):
        if password:
            self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def follow(self, user):
        if not self.is_following(user):
            f = Followed(follower=self, following=user)
            db.session.add(f)


    def unfollow(self, user):
        f = self.followed.filter_by(follower=self, following=user).first()
        if f:
            db.session.delete(f)


    def is_following(self, user):
        return self.followed.filter_by(follower=self, following=user).count() > 0


    def followed_posts(self):
        followed = Post.query.join(Followed, Followed.follower_id == self.id)\
                           .filter(Followed.following_id == Post.author_id)
        own = Post.query.filter_by(author_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())


    def to_json(self):
        json_user = {
            'username': self.username,
            'email': self.email,
            'about_me': self.about_me,
            'last_seen': self.last_seen,
            'posts': [post.to_json() for post in self.posts],
            'comments': [comment.to_json() for comment in self.comments]
        }
        return json_user