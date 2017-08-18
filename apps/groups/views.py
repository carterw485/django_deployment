from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from apps.groups.models import User, Group, Member
def logIn(request):
	if 'errors' in request.session:
		context = {
			'exists': True,
			'errors': request.session['errors'],
		}
	else:
		context = {
			'exists': False,
		}
	return render(request, 'groups/logIn.html', context)
def logout(request):
	if 'user' in request.session:
		del request.session['user']
	return redirect('/')
def logOrganizer(request):
	if 'errors' in request.session:
		del request.session['errors']
	if 'first_name' in request.POST:
		print type(request.POST['first_name'])
		print request.POST['first_name']
		if request.POST['first_name'].__len__ == 0 or request.POST['last_name'].__len__ == 0 or request.POST['username'].__len__ == 0 or request.POST['password'].__len__ == 0:
			print 'required fields'
			request.session['errors'] = 'All fields are required'
			return redirect('/')
		print 'registering'
		if User.objects.all().filter(username = request.POST['username']):
			request.session['errors'] = 'Username already exists'
			return redirect('/') 
		else:
			user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], username = request.POST['username'], password = request.POST['password'])
			user.save()
			print user
			return redirect('/')
	else:
		print 'logging in'
		if 'errors' in request.session:
			del request.session['errors']
		if User.objects.all().filter(username = request.POST['username']):
			user = User.objects.get(username = request.POST['username'])
			password = str(request.POST['password'])
			if password == user.password:
				print 'logged in successfully'
				request.session['user'] = user.id
				if 'errors' in request.session:
					del request.session['errors']
				return redirect('/groups/')
			else:
				request.session['errors'] = "bad log in credentials"
				return redirect('/')
		else:
			request.session['errors'] = "bad log in credentials"
			return redirect('/')
def multiOrganizer(request):
	if request.method == 'POST':
		print 'create'
		user = User.objects.get(id = request.session['user'])
		group = Group(name = request.POST['name'], description = request.POST['description'], created_by = user)
		print group
		group.save()
		group = Group.objects.get(name = request.POST['name'], description = request.POST['description'], created_by = user)
		print group.id
		members = Member(user = user, group = group)
		members.save()
		return redirect('/groups/')
	else:
		print 'get'
		if 'user' not in request.session:
			return redirect('/')
		members = Member.objects.all()
		user = User.objects.get(id = request.session['user'])
		groups = Group.objects.all()
		context = {
			'user': user,
			'groups': groups,
			'members': members,
			'counter': '|',
		}
		return render(request, 'groups/index.html', context)
def singleOrganizer(request, id):
	if request.method == 'DELETE':
		print 'delete'
		group = Group.objects.get(id = id)
		group.delete()
		print 'redirecting'
		return redirect('/groups')
	elif request.method == 'GET':
		print 'GET a single group'
		group = Group.objects.get(id = id)
		members = Member.objects.all().filter(group = group)
		user = User.objects.get(id = request.session['user'])
		isMember = False
		isCreator = False
		if group.created_by == user:
			isCreator = True
		for member in members:
			if member.user == user:
				isMember = True

		context = {
			'group': group,
			'members': members,
			'isCreator': isCreator,
			'isMember': isMember,
		}
		return render(request, 'groups/show.html', context)
def members(request, group_id):
	user = User.objects.get(id = request.session['user'])
	group = Group.objects.get(id = group_id)
	member = Member(user = user, group = group)
	member.save()
	return redirect('/groups/'+group_id)
def membersLeave(request, group_id):
	user = User.objects.get(id = request.session['user'])
	group = Group.objects.get(id = group_id)
	Member.objects.get(user = user, group = group).delete()
	return redirect('/groups/'+group_id)