from django.apps import apps
from tastypie.api import Api, Serializer
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL


def get_all_resourses():
    app_models = apps.all_models
    resources = []
    for app, models in app_models.items():
        for model, cls in models.items():
            resource_meta = type(
                'Meta',
                (),
                dict(
                    queryset=cls.objects.all(),
                    resourse_name='/'.join([app, model]),
                    formats=['json', ],
                    serializer=Serializer(formats=['json', 'plist']),
                    filtering={f.name: ALL for f in cls._meta.fields if cls._meta.fields},
                    ordering=[f.name for f in cls._meta.fields if cls._meta.fields],
                    authorization=Authorization(),
                )
            )
            resource = type(
                '%sResource' % str(cls._meta.object_name),
                (ModelResource,),
                dict(
                    _meta=resource_meta(),
                    Meta=resource_meta,
                )
            )
            resources.append(resource)
    return resources


v1_api = Api(api_name='v1')
v1_api.serializer = Serializer(formats=['json', ], content_types={'json': 'application/json', })
resources = get_all_resourses()
for r in resources:
    v1_api.register(r())
