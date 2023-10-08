import base64
import io
import json

import requests
import soundfile


def paddlespeech_request(url, data):
    """
    构造PaddleSpeech所需的post请求
    """

    res = requests.post(
        url=url,
        data=json.dumps(data)
    )

    if res.status_code == 200:
        res = res.json()
    else:
        print("请求失败，错误代码：", res.status_code)
        res = None
    return res


tts_url = "http://192.168.3.9:8090/paddlespeech/tts"
data = {
    "text": "Good Morning",
    "spk_id": 0,
    "speed": 1.0,
    "volume": 1.0,
    "sample_rate": 0,
    # 这里先不保存，演示如何将base64编码还原成wav音频
    "save_path": None,
    "lang": 'en'
}

res = paddlespeech_request(tts_url, data)

# 检查是否成功
print(res['success'])
print(res)

# 将res中的base64还原成wav

# wav_base64 = res['result']['audio']
# audio_data_byte = base64.b64decode(wav_base64)
# # 重新读取sample
# samples, sample_rate = soundfile.read(
#     io.BytesIO(audio_data_byte), dtype='float32')
# # 保存成audio
# outfile = "D:/ai/paddle/speech/output_tts.wav"
# soundfile.write(outfile, samples, sample_rate)
