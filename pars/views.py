from django.shortcuts import render
from .models import Fl, Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import *
from .forms import FlForm, TagForm
from django.shortcuts import redirect
from django.urls import reverse
import datetime

from django.core.paginator import Paginator
from django.db.models import Q


from rest_framework.viewsets import ModelViewSet
from pars.serializers import Serializer


class OrderView(ModelViewSet):
	queryset = Fl.objects.all()
	# q_date = '2020-02-01' #datetime.date.today()
	# print('-------', q_date)
	# queryset = Fl.objects.filter(date_p=q_date)
	serializer_class = Serializer
	# http://127.0.0.1:5000/pars/api/fl/?format=json


def index(request):
	search_query = request.GET.get('search', '')
	if search_query:
		flsz = Fl.objects.filter(Q(date_p__icontains=search_query) | Q(show__icontains=search_query) | Q(ref_link__icontains=search_query))
		paginator = Paginator(flsz, 10)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number()) + '&search={}'.format(search_query)
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number()) + '&search={}'.format(search_query)
		else:
			next_url = ''

		fllen = len(flsz)
		context = {
			'search_query': search_query,
			'fllen': fllen,
			'page_object': page,
			'is_paginated': is_paginated,
			'next_url': next_url,
			'prev_url': prev_url
		}
	else:
		flsz = Fl.objects.all()
		paginator = Paginator(flsz, 10)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number())
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number())
		else:
			next_url = ''
		# fl_ref_link = Fl.objects.all().values_list('ref_link')
		# for i in fl_ref_link:
		# 	print(i)
		fllen = len(flsz)
		context = {
			'fllen': fllen,
			'page_object': page,
			'is_paginated': is_paginated,
			'next_url': next_url,
			'prev_url': prev_url
		}

	return render(request, 'pars/index.html', context=context)

def index_today(request):
	q_date = datetime.date.today()
	# ref_y = refind_y(str(q_date))
	# ref_m = refind_m(str(q_date))
	# ref_d = refind_d(str(q_date))
	# ref_date = ref_y + '-' + ref_m + '-' + ref_d
	flsz = Fl.objects.filter(date_p=q_date)
	# fllen = len(flsz)
	# print(fllen)

	search_query = request.GET.get('search', '')
	if search_query:
		flsz = Fl.objects.filter(Q(date_p__icontains=q_date), Q(show__icontains=search_query) | Q(ref_link__icontains=search_query))
		paginator = Paginator(flsz, 10)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number()) + '&search={}'.format(search_query)
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number()) + '&search={}'.format(search_query)
		else:
			next_url = ''

		fllen = len(flsz)
		context = {
			'search_query': search_query,
			'fllen': fllen,
			'page_object': page,
			'is_paginated': is_paginated,
			'next_url': next_url,
			'prev_url': prev_url
		}
	else:
		paginator = Paginator(flsz, 10)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number())
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number())
		else:
			next_url = ''

		fllen = len(flsz)
		context = {
			'fllen': fllen,
			'page_object': page,
			'is_paginated': is_paginated,
			'next_url': next_url,
			'prev_url': prev_url
		}

	return render(request, 'pars/index_today.html', context=context) #{'flsz': flsz, 'fllen': fllen})

def refind_y(a):
	return a.split('-')[0]

def refind_m(a):
	return a.split('-')[1]

def refind_d(a):
	return a.split('-')[2]


class FlDetail(ObjectDetailMixin, View):
	model = Fl
	template = 'pars/detail.html'
	# def get(self, request):
	# 	form = FlForm()
	# 	return render(request, 'pars/detail.html', context={'form', form})


class FlUpdate(ObjectUpdateMixin, View):
	model = Fl
	model_form = FlForm
	template = 'pars/fl_update_form.html'




class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'pars/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
	model_form = TagForm
	template = 'pars/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'pars/tag_update_form.html'


class TagDelete(ObjectDeleteMixin, View):
	model = Tag
	template = 'pars/tag_delete_form.html'
	redirect_url = 'tags_list_url'


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'pars/tags_list.html', context={'tags': tags})