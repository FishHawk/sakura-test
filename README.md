# Sakura-13B-LNovel 模型轻小说翻译性能测试

Sakura-13B-Galgame 发布于[贴吧](https://tieba.baidu.com/p/8612129239)，[Huggingface](https://huggingface.co/SakuraLLM)。

本次实验旨在对比 Sakura0.8 和 0.9 版本之间的区别。

需要注意的是:

- 机器翻译小说的评价标准有些特殊。对于小说翻译来说，漏译或少量词语翻译错误可以接受，最重要的是要保持文本的通顺和风格。然而像“姐姐大人”被错误翻译成“大姐”这样改变了称呼和语气的错误，会严重影响小说的风格和读者的阅读感受。

- 对翻译结果的分析主要是挑错，目的是用来作为后续改进的参考。这并不表示 Sakura 效果不行，只是关注点不在 Sakura 模型的优点上。目前 Sakura 模型的优势是一眼可以看出的，无需测试。

- 小说链接里的 GPT 实际上用的是 Sakura 4bit 模型。个人感觉 4bit 和 8bit 区别不大，8bit 与其说会修复问题，不如说只是出问题的地方变了。

- 测试全是我个人判断，我的日语水平约在认识五十音，会网上搜字典这一档。

## 测试结果

- **[TB1:和風ファンタジーな鬱エロゲーの名無し戦闘員に転生したんだが周囲の女がヤベー奴ばかりで嫌な予感しかしない件](https://books.fishhawk.top/novel/hameln/232822)**

  - [测试章节](https://books.fishhawk.top/novel/hameln/232822/5) / [翻译对比](https://github.com/FishHawk/sakura-test/blob/main/tb1.translation.txt) / [错误分析](https://github.com/FishHawk/sakura-test/blob/main/tb1.report.md)
  - 章节特点：很多长句。

- **[TB2:大ハズレだと追放された転生重騎士はゲーム知識で無双する](https://books.fishhawk.top/novel/syosetu/n8465gx)**

  - [测试章节](https://books.fishhawk.top/novel/syosetu/n8465gx/18) / [翻译对比](https://github.com/FishHawk/sakura-test/blob/main/tb2.translation.txt) / [错误分析](https://github.com/FishHawk/sakura-test/blob/main/tb2.report.md)
  - 章节特点：网游，存在状态表。
  - 测试结果：0.9 整体来说更加准确，不过提升不大。一些专有名词翻译也更加稳定。值得一提的是，0.9 出现了错行。

- **[TB3:腹ペコ要塞は異世界で大戦艦が作りたい](https://books.fishhawk.top/novel/syosetu/n2749hf)**

  - [测试章节](https://books.fishhawk.top/novel/syosetu/n2749hf/4) / [翻译对比](https://github.com/FishHawk/sakura-test/blob/main/tb3.translation.txt) / [错误分析](https://github.com/FishHawk/sakura-test/blob/main/tb3.report.md)
  - 章节特点：科幻，很多片假名的专有名词。
  - 测试结果：0.9 整体来说更加准确，不过提升不大。0.9 理解的专有名词更多。

- **[TB4:今村司の逆転性活](https://books.fishhawk.top/novel/syosetu/n4885cd)**

  - [测试章节](https://books.fishhawk.top/novel/syosetu/n4885cd/2) / [翻译对比](https://github.com/FishHawk/sakura-test/blob/main/tb4.translation.txt) / [错误分析](https://github.com/FishHawk/sakura-test/blob/main/tb4.report.md)
  - 章节特点：R18，贞操逆转。
  - 测试结果：0.9 整体来说更加准确，不过提升不大。0.9 用词比较直白，更倾向保持原文结构。
