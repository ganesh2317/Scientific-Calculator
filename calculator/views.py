from django.shortcuts import render
from django.http import JsonResponse
import math
import re

def index(request):
	return render(request, 'calculator/index.html')

def calculate(request):
	if request.method == 'POST':
		expr = request.POST.get('expression', '')
		try:
			result = safe_eval(expr)
			return JsonResponse({'result': result})
		except Exception as e:
			return JsonResponse({'result': 'Error'})
	return JsonResponse({'result': ''})

def safe_eval(expr):
	# Only allow numbers, operators, parentheses, and math functions
	allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
	allowed_names['abs'] = abs
	allowed_names['pow'] = pow
	# Replace '^' with '**' for power
	expr = expr.replace('^', '**')
	# Remove any unwanted characters
	if not re.match(r'^[\d\s\+\-\*/\^\(\)\.,a-zA-Z]+$', expr):
		raise ValueError('Invalid characters in expression')
	# Evaluate the expression
	return eval(expr, {"__builtins__": {}}, allowed_names)
