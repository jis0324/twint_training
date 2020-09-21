import os
import twint

base_dir = os.path.dirname(os.path.abspath(__file__))

class Profile:
  # init
  def __init__(self):
    self.users_list = list()
    self.get_users_list()
    print(self.users_list)

  # get users list
  def get_users_list(self):
    users_list_file = "{}/userlist.txt".format(base_dir)
    if os.path.isfile(users_list_file):
      with open(users_list_file, 'r') as users_list_txt:
        self.users_list=[row.rstrip('\n') for row in users_list_txt]
    else:
      print("----- Not Fount userlists.txt File -----")

  # get profile of user
  def get_user_profile(self, username):
    # Configure
    c = twint.Config()
    c.Username = username
    c.Store_object = True
    twint.run.Lookup(c)
    # c.Username = username
    # c.User_full = True
    # c.Custom["user"] = ["bio"]
    # c.Profile_full = True
    # c.Search = "season"
    # c.Limit = 10
    # c.Until = "2019-12-01"
    # c.Format = "Tweet id: {id} | Username {username} | Date: {date} | Time: {time} | Tweet: {tweet}"
    # c.Output = "Tweet_File"
    # c.User_full = False
    # c.Profile_full = True
    # c.Retweets = False
    # c.Limit = 10
    # c.Store_csv = True
    # c.Output = "users.csv"
    # Run
    # twint.run.Lookup(c)
    # twint.run.Profile(c)
    # twint.run.Followers(c)
    # twint.run.Following(c)
    # twint.run.Favorites(c)
    # twint.run.Search(c)

  # main
  def main(self):
    if self.users_list:
      for index, username in enumerate(self.users_list):
        print("{}th User / Total {} Users : {}".format(index+1, len(self.users_list), username))
        self.get_user_profile(username)
    else:
      print("----- Empty Users List, Please Fill Out Users and Try again. -----")
      return


if __name__ == '__main__':
  profile = Profile()
  profile.main()