# import timm

# m = timm.create_model('mobilenetv3_large_100', pretrained=True)
# m.eval()

# import timm
# from pprint import pprint
# model_names = timm.list_models(pretrained=True)
# pprint(model_names)

import timm
from pprint import pprint
model_names = timm.list_models('*resne*t*')
pprint(model_names)