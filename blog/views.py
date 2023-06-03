from django.shortcuts import render, get_object_or_404
from .models import Post1


import markdown




def post_list(request):
    posts = Post1.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post1,pk=pk)
    post.body = markdown.markdown(post.body)
    return render(request, 'blog/post_detail.html', {'post': post})

def aboutme(request):
	bio=markdown.markdown('''Meet Siddharth Kinger, the fitness freak and textile tycoon! Born into 
	 textiles family, Siddharth transformed their business into a thriving empire. 
	 hen he's not crushing the competition, you'll find him pumping iron at the 
	 gym or sweating it out on a basketball court. He believes in the power of 
	 fitness to boost both his business acumen and his biceps. Not only does 
	 he inspire his employees to stay fit with in-office workouts, but he also 
	 gives back to the community through charitable endeavors. 
	 Siddharth Kinger: the man who tackles the business world with muscles to
	 match!''')

	return render(request,'blog/aboutme.html',{'bio':bio})

