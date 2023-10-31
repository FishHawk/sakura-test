import requests

endpoint = "http://192.168.1.162:6002/api/v1/generate"

prompt = "<reserved_106>将下面的日文文本翻译成中文：test<reserved_107>"
request = {
    "prompt": prompt,
    "auto_max_new_tokens": False,
    "max_tokens_second": 0,
    # Generation params. If 'preset' is set to different than 'None', the values
    # in presets/preset-name.yaml are used instead of the individual numbers.
    "preset": "None",
    "max_new_tokens": 1024,
    "do_sample": True,
    "temperature": 0.1,
    "top_p": 0.3,
    "repetition_penalty": 1.0,
    "num_beams": 1,
    "typical_p": 1,
    "epsilon_cutoff": 0,  # In units of 1e-4
    "eta_cutoff": 0,  # In units of 1e-4
    "tfs": 1,
    "top_a": 0,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "repetition_penalty_range": 0,
    "top_k": 40,
    "min_length": 0,
    "no_repeat_ngram_size": 0,
    "penalty_alpha": 0,
    "length_penalty": 1,
    "early_stopping": False,
    "mirostat_mode": 0,
    "mirostat_tau": 5,
    "mirostat_eta": 0.1,
    "grammar_string": "",
    "guidance_scale": 1,
    "negative_prompt": "",
    "seed": -1,
    "add_bos_token": True,
    "truncation_length": 2048,
    "ban_eos_token": False,
    "custom_token_bans": "",
    "skip_special_tokens": True,
    "stopping_strings": [],
}

response = requests.post(endpoint, json=request)
result = response.json()["results"][0]["text"]

print(result)
