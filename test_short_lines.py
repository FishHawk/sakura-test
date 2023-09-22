from sakura import *


if __name__ == "__main__":
    testbed = [
        "エレインに協力する代わりに仲介を頼んだ。",
        "傭兵ギルド……身も蓋もない表現をすれば荒事専門の口入れ屋である。",
        "目眩を起こしそうなほど高い天井と寒々しささえ感じさせる広い室内……中心に馬蹄型の机が置かれ、ソークは自由都市国家群の中央に、十人の男が左右を固めるように座している。",
        "袋の中を確認するようなマネはしない。",
        "「軽口を楽しむくらいの余裕がないと、足下を掬われるわよ」",
    ]

    for s in testbed:
        obj = translate_line_p(s)
        content = obj["choices"][0]["message"]["content"]
        print(content.strip())
