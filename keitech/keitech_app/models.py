from django.db import models



#newsletter model

class NewsLetter(models.Model):
    """This will create model for the newsletter"""
    email = models.EmailField(unique=True)


    def __str__(self):
        """This will return the string representation of the newsletter model"""
        self.email


#contacts model

class Contacts(models.Model):
    """This will create model for contacts model"""
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    comments = models.TextField()

    def __str__(self):
        """This will return the string representation for the contact model"""
        return self.name


# SignUp models

class SignUp(models.Model):
    """This will create the models for the signup users"""
    WINTECH = 'Women in tech'
    CITECH = 'Children in tech'
    VOLUNTEER = 'Volunteer'
    PARTNER = 'Partner'
    applyingas_choices = [
        (WINTECH, 'Women in tech'),
        (CITECH, 'Children in tech'),
        (VOLUNTEER, 'Volunteer'),
        (PARTNER, 'Partner'),
    ]
    First_Name = models.CharField(max_length=256, null=True)
    Last_Name = models.CharField(max_length=256, null=True)
    Nick_Name = models.CharField(max_length=256, null=True)
    Phone = models.PositiveIntegerField(null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    retype_password = models.CharField(max_length=200)
    applying_as = models.CharField(
        max_length=100,
        choices = applyingas_choices,
        default = PARTNER
        )
    applying_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        """This will return the string representation of the signup model"""
        return self.First_Name


# Question models

class Question(models.Model):
    """This will create a question model"""
    user_name = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    details = models.TextField()
    Added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """This will return the string representation of the question model"""
        return self.title


# Answer models
class Answer(models.Model):
    """This will create the answer models"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    details = models.TextField()
    Added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """This will return the string representation of the answer model"""
        return self.details


#Comments models

class Comments(models.Model):
    """This will create the comment models"""
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_name = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='comment_user')
    Added_on = models.DateTimeField(auto_now_add=True)


#upvote models

class UpVote(models.Model):
    """This will create the upvote models"""
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_name = models.ForeignKey(SignUp, on_delete=models.CASCADE,related_name='upvote_user')

#Downvote models
class DownVote(models.Model):
    """This will create the downvote models"""
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_name = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='downvote_user')
