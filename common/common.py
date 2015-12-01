#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""自定义Faker-Factory Providers.
"""

from __future__ import unicode_literals, print_function

from random import randint, sample
from string import digits, ascii_lowercase

import pymongo
from faker import Faker
from faker.providers import BaseProvider
from testdata import Factory


class CountFromCollection(Factory):
    """从数据集中的最小值开始依次取值, 仿FieldFromCollection添加新的类型.
        (from testdata.extra.mongodb import FieldFromCollection)
    """

    def __init__(self, database, collection, field_name, filter_query={}, **connection_kw):
        super(CountFromCollection, self).__init__()
        with pymongo.MongoClient(**connection_kw) as client:
            db = client[database]
            collection = db[collection]
            self._possible_values = collection.find(filter_query).distinct(field_name)

    def __call__(self):
        return self._possible_values[self.current_index]


class ChinaProvider(BaseProvider):
    allowed_chars = ascii_lowercase + digits
    email_domains = ('126.com', 'qq.com', '163.com')

    cn_tag_data = [
        "女生", "情侣", "霸气", "伤感", "个性", "男生", "超拽", "唯美", "森系",
        "原创", "搞笑", "爱情", "非主流", "好听", "文艺", "姐妹", "校园", "幸福",
        "可爱", "古风", "回忆", "小清新", '锥子脸', "美女", "美文", "逗比", "卖萌"
    ]

    cn_bio_data = [
        "生活是一面镜子。你对它笑，它就对你笑；你对它哭，它也对你哭。",
        "活着一天，就是有福气，就该珍惜。当我哭泣我没有鞋子穿的时候，我发现有人却没有脚。",
        "人生是个圆，有的人走了一辈子也没有走出命运画出的圆圈，其实，圆上的每一个点都有一条腾飞的切线。",
        "千万别迷恋网络游戏，要玩就玩好人生这场大游戏。",
        "命运负责洗牌，但是玩牌的是我们自己！",
        "我们心中的恐惧，永远比真正的危险巨大的多。",
        "命运掌握在自己手中。要么你驾驭生命，要么生命驾驭你，你的心态决定你是坐骑还是骑手。",
        "宁愿做过了后悔，也不要错过了后悔。",
        "不要拿小人的错误来惩罚自己，不要在这些微不足道的事情上折磨浪费自己的宝贵时间。",
        "如果我们都去做自己能力做得到的事，我们会让自己大吃一惊。",
        "出路出路，走出去了，总是会有路的。困难苦难，困在家里就是难。",
        "学的到东西的事情是锻炼，学不到的是磨练。",
        "过错是暂时的遗憾，而错过则是永远的遗憾！",
        "环境不会改变，解决之道在于改变自己。",
        "勇气是控制恐惧心理，而不是心里毫无恐惧。",
        "还能冲动，表示你还对生活有激情，总是冲动，表示你还不懂生活。",
        "在实现理想的路途中，必须排除一切干扰，特别是要看清那些美丽的诱惑。",
        "人一生下就会哭，笑是后来才学会的。所以忧伤是一种低级的本能，而快乐是一种更高级的能力。",
        "两个人共尝一个痛苦只有半个痛苦，两个人共享一个欢乐却有两个欢乐。",
        "放弃该放弃的是无奈，放弃不该放弃的是无能，不放弃该放弃的是无知，不放弃不该放弃的是执著！",
        "行动是治愈恐惧的良药，而犹豫、拖延将不断滋养恐惧。",
        "你把周围的人看作魔鬼，你就生活在地狱；你把周围的人看作天使，你就生活在天堂。",
        "人之所以痛苦，在于追求错误的东西。",
        "与其说是别人让你痛苦，不如说自己的修养不够。",
        "如果你不给自己烦恼，别人也永远不可能给你烦恼，烦恼都是自己内心制造的。",
        "好好管教自己，不要管别人。",
        "你硬要把单纯的事情看得很严重，那样子你会很痛苦。",
        "一杯清水因滴入一滴污水而变污浊，一杯污水却不会因一滴清水的存在而变清澈。",
        "运气就是机会碰巧撞到了你的努力。",
        "得之坦然，失之淡然，顺其自然，争其必然。",
        "时间是治疗心灵创伤的大师，但绝不是解决问题的高手。",
        "天道酬勤。也许你付出了不一定得到回报，但不付出一定得不到回报。",
        "逆境是成长必经的过程，能勇于接受逆境的人，生命就会日渐的茁壮。",
        "只有不断找寻机会的人才会及时把握机会。",
        "做一个决定，并不难，难的是付诸行动，并且坚持到底。",
        "如果你能像看别人缺点一样，如此准确的发现自己的缺点，那么你的生命将会不平凡。",
        "无论你觉得自己多么的了不起，也永远有人比你更强；无论你觉得自己多么的不幸，永远有人比你更加不幸。",
        "背负着过去的痛苦，夹杂着现实的烦恼，这对于人的心灵而言是无任何益处。",
        "只有你学会把自己已有的成绩都归零，才能腾出空间去接纳更多的新东西，如此才能使自己不断的超越自己。",
        "人生是一条没有回程的单行线，上帝不会给你一张返程的票。",
        "对待生活中的每一天若都像生命中的最后一天去对待，人生定会更精彩。",
        "活在昨天的人失去过去，活在明天的人失去未来，活在今天的人拥有过去和未来。",
        "忍别人所不能忍的痛，吃别人所别人所不能吃的苦，是为了收获得不到的收获。",
        "大部分人往往对已经失去的机遇捶胸顿足，却对眼前的机遇熟视无睹。",
        "一个懒惰的少年将来就是一褴褛的老人。",
        "困难是一块顽石，对于弱者它是绊脚石，对于强者它是垫脚石。",
        "笑对人生，能穿透迷雾；笑对人生，能坚持到底；笑对人生，能化解危机；笑对人生，能照亮黑暗。",
        "人生最大的悲哀不是失去太多，而是计较太多，这也是导致一个人不快乐的重要原因。",
        "我们总是对陌生人太客气，而对亲密的人太苛刻。",
        "人的一生就像一篇文章，只有经过多次精心修改，才能不断完善。",
        "虽然我们无法改变人生，但可以改变人生观。虽然我们无法改变环境，但我们可以改变心境。",
        "如果你还认为自己还年轻，还可以蹉跎岁月的话，你终将一事无成，老来叹息。",
        "当你快乐时，你要想，这快乐不是永恒的。当你痛苦时，你要想，这痛苦也不是永恒的。",
        "命运就像自己的掌纹，虽然弯弯曲曲，却永远掌握在自己手中。",
        "不要浪费你的生命，在你一定会后悔的地方上。",
        "激情，这是鼓满船帆的风。风有时会把船帆吹断；但没有风，帆船就不能航行。",
        "人是可以快乐地生活的，只是我们自己选择了复杂，选择了叹息！",
        "不管从什么时候开始，重要的是开始以后不要停止；不管在什么时候结束，重要的是结束以后不要后悔。",
        "抱最大的希望，为最大的努力，做最坏的打算。",
        "人生最大的错误是不断担心会犯错。",
        "忌妒别人，不会给自己增加任何的好处，忌妒别人，也不可能减少别人的成就。",
        "长得漂亮是优势，活得漂亮是本事。",
        "大多数人想要改造这个世界，但却罕有人想改造自己。",
        "每个人都有潜在的能量，只是很容易被习惯所掩盖，被时间所迷离，被惰性所消磨。",
        "积极的人在每一次忧患中都看到一个机会，而消极的人则在每个机会都看到某种忧患。",
        "创造机会的人是勇者，等待机会的人是愚者。",
        "旁观者的姓名永远爬不到比赛的计分板上。",
        "同样的瓶子，你为什么要装毒药呢？同样的心理，你为什么要充满着烦恼呢？",
        "放弃谁都可以，千万不要放弃自己！71、人生是一场旅行，在乎的不是目的地，是沿途的风景以及看风景的心情。",
        "再长的路，一步步也能走完，再短的路，不迈开双脚也无法到达。",
        "多一分心力去注意别人，就少一分心力反省自己。",
        "人生就像钟表，可以回到起点，却已不是昨天！",
        "人生就像弈棋，一步失误，全盘皆输。",
        "在必要时候需要弯一弯，转一转，因为太坚强容易折断，我们需要更多的柔软，才能战胜挫折。",
        "自以为拥有财富的人，其实是被财富所拥有。",
        "人生就像一个动物园，当你以为你在看别人耍猴的时候，却不知自己也是猴子中的一员！",
        "从绝望中寻找希望，人生终将辉煌。",
        "你不能左右天气，但可以改变心情。你不能改变容貌，但可以掌握自己。你不能预见明天，但可以珍惜今天。",
        "尝试去把别人拍过来的砖砌成结实的地基，生活就不会那么辛苦了。",
        "行动不一定带来快乐，而无行动则决无快乐。",
        "你可以一无所有，但绝不能一无是处。",
        "突破心理障碍，才能超越自己。",
        "如果我们有着快乐的思想，我们就会快乐；如果我们有着凄惨的思想，我们就会凄惨。",
        "面对困境，悲观的人因为往往只看到事情消极一面。",
        "不要因为自己还年轻，用健康去换去金钱，等到老了，才明白金钱却换不来健康。",
        "你不要一直不满他人，你应该一直检讨自己才对。",
        "心念一转，万念皆转；心路一通，万路皆通。",
        "愚昧者怨天尤人，无能者长吁短叹，儒弱者颓然放弃。",
        "智者用无上心智和双手为自己开辟独有的天空，搭建生命的舞台。",
        "时间是小偷，他来时悄无声息，走后损失惨重，机会也是如此。",
        "成功的关键在于相信自己有成功的能力。",
        "人的缺点就像花园里的杂草，如果不及时清理，很快就会占领整座花园。",
        "滴水穿石不是靠力，而是因为不舍昼夜。",
        "相信自己能力的人，任何事情都能够做到。",
        "把事情办好的秘密就是行动。成功之路就是有条理思考之后的行动！行动！行动！"
    ]

    cn_message_data = [
        "大师兄到此一游！", "顶一个！", "赞一个！", "大家快来看呀！", "你说得咋这么对恁！",
        "不必给我爱，不必给我钱，不必给我名誉，给我真理吧。——梭罗",
        "只有两种人最具有吸引力，一种是无所不知的人，一种是一无所知的人。——王尔德《道连·葛雷的画像》",
        "外国的英雄都是成年之后才出来打怪兽的，只有我们国家的葫芦娃一出生就开始打妖怪。——中国孩子压力大",
        "生活需要减负，减负从非应酬式交往开始。——林特特",
        "大吃小，是实力!小吃大，是智力!大小通吃，是权力!——周立波",
        "保守秘密；忘记别人对你的伤害；不浪费时间。——世上最难的三件事",
        "理想的社会，应该是国家有目标、社会有共识、个人有希望。——缺失任何一种，我们的社会就不和谐",
        "不说泄气话，不发牢骚，不找借口，早睡早起，每天跑十公里，坚持每天写十页，要像个傻瓜似的。——日本作家村上春树的生活准则",
        "生于坚守良知，死于践踏伦理。",
        "我不够聪明，但勤能补拙。这个世界是有平衡的，当你发现自己有缺点的时候，会用另外的优点去弥补它，最后达到平均线上。",
        "好男人要做到的不过就是：一、能挣到给女人买裙子的钱；二、陪她去买；三、说她穿上裙子好看。——网上流传的情感语录",
        "无知的焦虑从来都是错的，而过于忙碌的人一定会迷失方向——出自《圣经·箴言》的这句训诫对现代人来说并不过时",
        "人只有经历自己的渺小，才能到达高尚。——卡夫卡《箴言》",
        "以前愁能不能吃饱，现在愁会不会吃倒。——感悟",
        "中国高考有万千毛病，却是目前最公平的一种方式。没有高考，你拼得过富二代吗？——白岩松在郑州大学演讲时说",
        "5岁：我给你报少年宫。7岁：我给你报奥数班。15岁：我给你报重点中学。18岁：我给你报高考突击班。23岁：我给你报考公务员。32岁：我给你报了《非诚勿扰》",
        "正确结论来自多元的声音，而不是权威的选择。——《批评官员的尺度》",
        "错的事情我们都敢做，对的事情反而不敢做了，那还活着干吗，还不如去死。——影片《窃听风云》台词",
        "国人现在不是根据菜单吃饭，而是按照“元素周期表”吃饭。——时寒冰",
        "对未来的真正慷慨，是把一切献给现在。——加缪",
        "我买过最贵的东西，是梦想！——台湾作家九把刀为圆导演梦，不惜倾家荡产，拍出他的首部电影",
        "幸福如果作为生活的副产品，是很棒的一个东西，但把它作为目标来追求，只会导致灾难。——斯沃斯莫尔学院社会学教授巴里·施瓦兹",
        "主宰国家命运的，不是桌面上争个不休的政治人物，而是摇篮边的那双手。——蒙哥马利将军",
        "钢琴弹得好加分，那杀猪杀得好，凭什么不给加分？——有感于高考加分项目繁多且屡屡出现加分造假，一位教授如是说",
        "言辞越空洞，观点就越复杂。——一条经验法则",
        "无辱骂、无歧视、无骚扰、无虐待。——东莞一家鞋厂招聘启事的“保证条款”",
        "人生就是一场未知目的地的旅行，更多的时候，我们并不知道自己接下来会遇见怎样的未来。只不过有时候，我们只是一味地狂奔，却忘记了旅行的意义。"
    ]

    def cn_email(self):
        character = ''.join(sample(self.allowed_chars, randint(4, 10)))
        return character + '@' + self.random_element(self.email_domains)

    def cn_bio(self):
        return self.random_element(self.cn_bio_data)

    def cn_tag(self):
        return self.random_element(self.cn_tag_data)

    def cn_message(self):
        return self.random_element(self.cn_message_data)


def test():
    """测试新建Provider.
    """

    fake = Faker()
    fake.add_provider(ChinaProvider)

    for _ in range(10):
        print(fake.cn_email())
        print(fake.cn_tag())


if __name__ == '__main__':
    """测试.
    """

    test()
