def create_youtube_video(title,description):
	new_vid={"title":title , "description": description , "likes" : 0 , "dislikes" : 0 , "comments":{"",""}};
	return new_vid;
def like(new_vid):
	if "likes" in new_vid:
		new_vid["likes"]+=1;
def like(new_vid):
	if "dislikes" in new_vid:
		new_vid["dislikes"]+=1;
def add_comment(new_vid{},username,comment_text):
	new_vid["comments"]["username"]=new_vid["comments"]["comment_text"]
	return new_vid;
vid_first=create_youtube_video("15","13")