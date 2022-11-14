import user
import post

app_user_1 = user.User("al@al.com", "Al Sharma", "pwd1", "DevOps Manager")
app_user_1.get_user_info()

app_user_2 = user.User("Sal@Sal.com", "Sal Sharma", "pwd2", "DevOps Engineer")
app_user_2.get_user_info()

new_post = post.Post("on a secret mission today", app_user_2.name)
new_post.get_post_info()