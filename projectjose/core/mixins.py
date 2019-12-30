from django.db.models import Q
from django.contrib.auth.mixins import AccessMixin



class SearchEnabledViewMixin:
    search_fileds = []
    search_results_count = None

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search', None)
        search_expr = None

        if search is not None:
            for i, field in enumerate(self.search_fileds):
                if i == 0:
                    search_expr = Q(**{f'{field}__icontains': search})
                else:
                    search_expr = search_expr | Q(
                        **{
                            f'{field}__icontains': search
                        }
                    )
        if search_expr is not None:
            qs = qs.filter(search_expr)
            self.search_results_count = qs.count()
            return qs

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['use_simple_search'] = len(self.search_fileds) > 0
        context['is_searching'] = 'search' in self.request.GET
        context['search_results_count'] = self.search_results_count
        return context


class FilterEnabledViewMixin:
    filter = None
    filter_class = None
    filter_form_class = None
    filter_form_class = None
    advanced_search_form_class = None

    def get_filter_class(self):
        return self.filter_class

    def get_filter(self):
        filter_class = self.get_filter_class()

        if filter_class is not None:
            qs = super().get_queryset()
            self.filter = self.get_filter_class()(self.request.GET, queryset=qs)
            return self.filter

        return None

    def get_queryset(self):
        return getattr(
            self.get_filter(),
            'qs',
            super().get_queryset()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        if self.filter_form_class:
            context['filter_form'] = self.filter_form_class(
                data=self.request.GET
            )
        if self.advanced_search_form_class:
            context['advanced_search_form'] = self.advanced_search_form_class(
                data=self.request.GET
            )
        if self.filter_class:
            context['is_filtering'] = any([
                key in self.request.GET for key in
                dict(self.filter_class.get_filters()).keys()
            ])
        else:
            context['is_filtering'] = False

        return context
