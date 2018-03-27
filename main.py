from mvatv.plugin.data_sources.zimuzu import ZIMUZU
from mvatv.utils.utils import Quality
import traceback

z = ZIMUZU()
try:
    print(z.search('闪电侠', 4, 1, Quality.Low, False))
except Exception as e:
    print(traceback.format_exc())