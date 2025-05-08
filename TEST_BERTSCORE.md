# Translation Evaluation Results

## Individual Sample Results

### Sample 1

**English:**
```
Last week, the broadcast of period drama “Beauty Private Kitchen” was temporarily halted, and accidentally triggered heated debate about faked ratings of locally produced dramas.
```

**Reference Chinese:**
```
上周，古装剧《美人私房菜》临时停播，意外引发了关于国产剧收视率造假的热烈讨论。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    上周，电视剧《美丽人生厨房》的播出被临时中断，意外引发了关于本土剧虚假收视率争议。
    ```
*   **STUDENT:**
    ```
    上星期，电视剧《私人厨房》的播映被暂时暂停，并因本地制作的剧集虚假评分引发了一场激烈的辩论。
    ```
*   **TEACHER_PEFT:**
    ```
    上周，古装剧《私人厨房》的播放被临时中断，这意外引发了关于本地制作电视剧虚假收视率的大讨论。
    ```
*   **STUDENT_PEFT:**
    ```
    上周，由《私人厨房》（Private Kitchen ） 节目的播送暂时中断，意外引发了对本地制作的剧集虚假评分的激烈争论。
    ```
*   **HLKD:**
    ```
    上周，播出了名为“私人厨房的美丽”（Beauty Private Kitchen）的电视节目暂时停止播放，并引发了关于假制片人评分本地剧集的激烈争论。
    ```
*   **SLKD:**
    ```
    上个月播出的“美丽私人厨房 ” 一度被暂时停止，而意外地引发了对当地制作戏剧的虚假评价。
    ```

---

### Sample 2

**English:**
```
Civil rights group issues travel warning for Missouri
```

**Reference Chinese:**
```
民权团体针对密苏里州发出旅行警告
```

**Model Outputs:**
*   **TEACHER:**
    ```
    民权组织发布警告，敦促前往密苏里州的人注意安全。
    ```
*   **STUDENT:**
    ```
    民权团体发出撤离通知，要求避免前往密苏里州
    ```
*   **TEACHER_PEFT:**
    ```
    民权组织发出旅行警告，敦促人们不要前往密苏里州。
    ```
*   **STUDENT_PEFT:**
    ```
    民权组织向密尔沃基发出警告。
    ```
*   **HLKD:**
    ```
    民权团体发出警告，称在孟菲斯（Missouri）旅行是危险的。
    ```
*   **SLKD:**
    ```
    美国公民组织发出旅行警告
    ```

---

### Sample 3

**English:**
```
The National Association for the Advancement of Colored People has put out an alert for people of color traveling to Missouri because of the state's discriminatory policies and racist attacks.
```

**Reference Chinese:**
```
由于密苏里州的歧视性政策和种族主义袭击，美国有色人种促进协会 (NAACP) 向准备前往密苏里州出游的有色人群发出旅行警告。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    全国有色人种协进会已发布警告，提醒前往密苏里州的有色人种注意该州歧视性政策和种族攻击。
    ```
*   **STUDENT:**
    ```
    中国共产党全国代表大会也发布了关于因种族歧视和种族仇恨而旅行的黑人人的警告。
    ```
*   **TEACHER_PEFT:**
    ```
    全国有色人种促进会发布了一则警告，提醒人们因为该州的歧视性政策和种族主义攻击而计划前往密苏里州。
    ```
*   **STUDENT_PEFT:**
    ```
    美国有色人种进步协会发布了一封警告信，提醒因州政府的歧视政策和种族攻击而前往密苏里州旅行的人。
    ```
*   **HLKD:**
    ```
    美国有色人种联盟已经发出警告，因为该州的歧视政策和种族攻击而前往孟菲斯的人。
    ```
*   **SLKD:**
    ```
    国家红十字会呼吁那些肤色为黑人的旅行者前往孟加拉省，因为这些州在歧视政策和种族攻击方面存在差别。
    ```

---

### Sample 4

**English:**
```
"The NAACP Travel Advisory for the state of Missouri, effective through August 28th, 2017, calls for African American travelers, visitors and Missourians to pay special attention and exercise extreme caution when traveling throughout the state given the series of questionable, race-based incidents occurring statewide recently, and noted therein," the group's statement reads.
```

**Reference Chinese:**
```
“2017 年 8 月 28 日生效的 NAACP 密苏里州旅行咨询中呼吁，因近期密苏里州发生了一系列可疑的种族性事件，所有非裔美籍旅行者、游客以及密苏里州人在密苏里州旅行时应特别注意并采取极其谨慎的态度，特此告知，”该团体的声明宣称。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    美国公民大会对密苏里州旅行警告，有效期至2017年8月28日，呼吁所有非洲裔旅客、游客和密苏里州居民在全州范围内旅行时特别注意并采取极端谨慎措施。这是因为近期全省发生的一系列有争议的、基于种族的事件而引起的关注。该组织的声明如下。
    ```
*   **STUDENT:**
    ```
    纳拉克行动指南（针对美国俄亥俄州，有效至2017年8月28日）呼吁非洲裔旅行者、游客和俄亥俄人，在整个州内旅行时格外注意并采取极端警惕措施。根据最近在该州发生的系列不法事件的报道，以及其中所提到的内容，该团体声明如下：“NAACP行动指南”旨在提醒非洲裔旅行者、游客和俄亥俄人，在整个州内旅行时特别关注，并采取极端警惕措施。
    ```
*   **TEACHER_PEFT:**
    ```
    “密苏里州非裔美国人旅行警示，有效期至2017年8月28日 ， 强调黑人游客、访客和密苏里人应当特别注意并采取极端谨慎的措施在全州范围内出行。 这是因为近期一系列可疑、基于种族的事件在全国各地发生，这些事件被提到了警告中。”这一组织的声明说。
    ```
*   **STUDENT_PEFT:**
    ```
    美国黑人旅行咨询小组（NAACP）对肯塔基州的有效期限为2017年8月28日的建议称，非洲裔美国人、游客和肯塔基州的人士在乘坐该州所有道路时必须特别注意并采取极端谨慎的行为。
    ```
*   **HLKD:**
    ```
    《蒙大拿州旅行警告（Missouri Travel Alert）》（NAACP Travel Advisory for the state of Missouri，有效至2017年8月28日 ） ， 暂时称非洲裔美国人、游客和蒙大拿州人应特别注意并尽最大可能保持高度警惕，在整个州范围内，最近发生的几起种族偏见事件正在被该团体所提及。
    ```
*   **SLKD:**
    ```
    “美国全国旅行协会（NAACP）于2017年8月28日有效，对来自马萨诸塞州的旅者、游客以及莫里亚人来说给予特别的关注和在近期发生的种种可疑的种族性事件进行强调” ， 这组报告指出，在这些地区发生的问题中，美国旅行协会将给予非洲裔美国人、访客和穆斯林以特殊关注，并且当它们前往该地区时必须格外小心。
    ```

---

### Sample 5

**English:**
```
A recent Missouri law making it harder for people to win discrimination lawsuits, as well as the state's law enforcement disproportionately targeting minorities prompted the group to issue the travel alert, the NAACP said.
```

**Reference Chinese:**
```
NAACP 指出，最近通过的一项密苏里州法律使得人们更难赢得歧视诉讼，该州执法也一定程度上针对少数群体，这些现象促使该组织发布了旅行警告。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    近日，密苏里州通过的一项限制人们提起歧视诉讼的法律以及该州警察部门对少数族裔群体过度施压的行为引发了这个组织发布旅行警告，美国公民权利委员会表示。
    ```
*   **STUDENT:**
    ```
    近来的蒙大拿州法律使人们更容易获得歧视诉讼的判决，以及该州执法机构对少数族裔群体偏见的不当对待，引发了该团体发布旅行警告，美国非裔组织说。
    ```
*   **TEACHER_PEFT:**
    ```
    最近密苏里州通过的法律使得人们更难赢得歧视诉讼，以及该州警察对少数族裔的偏见性行为也引发了该组织发布旅行警告。 《全国有色人种协进会》（NAACP）表示。
    ```
*   **STUDENT_PEFT:**
    ```
    最近的马萨诸塞州法律使得人们很难获得歧视诉讼，而该州执法部门对少数群体的偏袒也引发了这一警告，该组织表示。
    ```
*   **HLKD:**
    ```
    最近的密尔沃基州法律使人们更容易获得歧视诉讼，而该省执法部门对少数族裔的偏见也引起了NAACP集团发出旅行警告。
    ```
*   **SLKD:**
    ```
    最近，一项由蒙代尔州要求人们更难获得歧视诉讼的法律，以及该州执法机构对少数族人群的特别执法导致该团体发出旅行警告，纳瓦克公司说。
    ```

---

### Sample 6

**English:**
```
"You have violations of civil rights that are happening to people.
```

**Reference Chinese:**
```
侵犯公民权利的行为正发生在人们身上。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    你有人权受到侵犯的情况。
    ```
*   **STUDENT:**
    ```
    你正在遭受着侵犯人权的行为。
    ```
*   **TEACHER_PEFT:**
    ```
    “你正在遭受违反人权的行为。 ”
    ```
*   **STUDENT_PEFT:**
    ```
    你正在践踏着人们的人权。
    ```
*   **HLKD:**
    ```
    您正在发生的侵犯公民权利的行为正侵害着人们。
    ```
*   **SLKD:**
    ```
    人们在非法使用公民权利的行为中出现了违法行为。
    ```

---

### Sample 7

**English:**
```
They're being pulled over because of their skin color, they're being beaten up or killed," the president of the Missouri NAACP, Rod Chapel, told The Kansas City Star.
```

**Reference Chinese:**
```
他们因肤色被停车盘问，被殴打或被杀害，”密苏里州 NAACP 主席罗德·查培尔告诉堪萨斯城星报 (The Kansas City Star)。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    他们因为肤色被拦下，被打或被杀，“密苏里州黑人民权协会主席罗德·查尔 chapel 说，这是《堪萨斯城星报》的报道。
    ```
*   **STUDENT:**
    ```
    他们被拘留是因为肤色，被打或杀死，“马萨诸塞纳道反对党总统罗伯特·查普曼”（Rod Chapel）告诉《堪萨斯城星报》。
    ```
*   **TEACHER_PEFT:**
    ```
    因为肤色，他们被警察拦截；遭到殴打或杀害。 ” 毛里塔尼亚黑人公民委员会主席罗德·查尔琴（Rod Chapel）告诉《堪萨斯城星报》。
    ```
*   **STUDENT_PEFT:**
    ```
    这些被贴上有色眼镜的黑人因为肤色而受到迫害，或者被打死，“ 去年当选总统的密西西比纳达尔党主席罗伯特·查普曼（Robert Chappell）告诉《堪萨斯城星报 》 。
    ```
*   **HLKD:**
    ```
    他们因为肤色而被拦截，被殴打或杀害，“孟菲斯纳粹主义民主党主席罗伯特·查普（Rod Chapel）告诉《堪萨斯城星报 》 。
    ```
*   **SLKD:**
    ```
    他们被拖下是因为肤色原因，受到攻击或者遭到杀戮。 这是蒙大拿纳德·阿帕克总统告诉《凯西斯星报》的记者说的。
    ```

---

### Sample 8

**English:**
```
"We are hearing complaints at a rate we haven't heard before."
```

**Reference Chinese:**
```
“我们收到了许多投诉，数量前所未有。”
```

**Model Outputs:**
*   **TEACHER:**
    ```
    我们正在听到比以往任何时候都更多的投诉。
    ```
*   **STUDENT:**
    ```
    我们正在听到投诉的数量，这在以前从未如此之高。
    ```
*   **TEACHER_PEFT:**
    ```
    我们听到的抱怨频率远比以前高。
    ```
*   **STUDENT_PEFT:**
    ```
    我们听到的抱怨数量与以前相比，已变得异常之大。
    ```
*   **HLKD:**
    ```
    我们听到的投诉比以前少得多。
    ```
*   **SLKD:**
    ```
    我们听到了一个频率比我们以前听到的高得令人震惊的投诉。
    ```

---

### Sample 9

**English:**
```
It is the first such warning that the organization has issued for a state in the US.
```

**Reference Chinese:**
```
这是该组织在美国针对某个州发布的第一个此类警告。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    这是该组织对美国州发出的第一个此类警告。
    ```
*   **STUDENT:**
    ```
    这是该组织首次发布警告，针对美国的一国。
    ```
*   **TEACHER_PEFT:**
    ```
    这是该组织向美国一个国家发出的首份警告。
    ```
*   **STUDENT_PEFT:**
    ```
    这是美国第一个警告组织的有关国家的一次。
    ```
*   **HLKD:**
    ```
    这是该组织首次发出警告，有关美国的国家。
    ```
*   **SLKD:**
    ```
    这是美国第一个警告。
    ```

---

### Sample 10

**English:**
```
The group cited incidents such as racial slurs against black students at the University of Missouri and the death of Tory Sanders, 28, a black man from Tennessee.
```

**Reference Chinese:**
```
该组织援引了密苏里大学对黑人学生的种族诽谤以及 28 岁田纳西州黑人男性托利·桑德斯的死亡事件。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    该团体列举了针对黑学生的种族侮辱事件，如密苏里大学的种族歧视行为，并提到在田纳西州28岁的黑人男子托比·桑德斯(Tory Sanders)死亡案。
    ```
*   **STUDENT:**
    ```
    该小组引用了关于黑学生种族歧视的事件，如莫尔兹克大学的种族侮辱和Tory Sanders先生，28岁，来自田纳西州的黑色人犯的死亡。
    ```
*   **TEACHER_PEFT:**
    ```
    该组织指出，如密苏里大学种族侮辱黑人学生和一名来自田纳西州的28岁黑人男子泰托·桑德斯（Tory Sanders）死亡等事件。
    ```
*   **STUDENT_PEFT:**
    ```
    该小组引用了黑人学生在马萨诸塞大学的种族歧视言论以及Tory Sanders，28岁来自田纳西州黑人的死亡事件。
    ```
*   **HLKD:**
    ```
    该小组列举了如蒙哥马利大学的种族歧视言论和Troy Sanders，28岁来自田纳西州黑人男子死亡事件。
    ```
*   **SLKD:**
    ```
    该组织指出的事件包括对美国大学黑人学生种族歧视事件以及28岁的英国人拉塞尔斯·桑德斯死亡。
    ```

---

### Sample 11

**English:**
```
Sanders died under questionable circumstances earlier this year after he ran out of gas while traveling through the state, and was taken into custody by Missouri police without being accused of a crime.
```

**Reference Chinese:**
```
今年早些时候，桑德斯在可疑情况下死亡。他在密苏里州旅行时燃油耗尽，被密苏里州警方在无指控犯罪的情况下拘留。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    桑德斯先生在今年早些时候因在州内旅行时因为缺油而死亡，被莫瑞州警方无罪拘捕。
    ```
*   **STUDENT:**
    ```
     Sanders 死亡在去年年底因途中无证行驶而欠账，被孟菲斯警方逮捕，未被指控任何犯罪。
    ```
*   **TEACHER_PEFT:**
    ```
    桑德斯在去年早些时候死于可疑的条件下，当时他在旅行中跑空了油箱，并被密苏里州警方无罪地拘捕。
    ```
*   **STUDENT_PEFT:**
    ```
    萨斯克在去年夏天因为开车途中耗尽了汽油而死亡，当时他正在行驶途经该州时被一辆警车带走，并且没有因此被捕。
    ```
*   **HLKD:**
    ```
     Sanders 死于去年年底，当时他正在通过州道旅行，但因为没有足够的汽油而被送进警察局。 由于没有犯罪的嫌疑，他被无罪释放。
    ```
*   **SLKD:**
    ```
    萨尔科奇在去年跑出州时，因为途中未带足汽油而被警察带走，并被关押在了蒙大拿州。
    ```

---

### Sample 12

**English:**
```
The advisory also points to a recent report by the Missouri Attorney General's Office showing that black drivers in the state were 75 percent more likely to be pulled over than whites.
```

**Reference Chinese:**
```
咨询中还指出，密苏里州总检察长办公室最近的一份报告显示，“与白人相比，该州的黑人司机被停车盘查的可能性要高出 75%”。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    该指导原则还指出，最近由密苏里州律师厅发布的报告表明，在该州，黑人司机比白人司机被拦截的可能性高出75%。
    ```
*   **STUDENT:**
    ```
    该建议也指出，由孟菲斯州 attorney general的办公室最近发布的报告表明，在该州，黑人驾驶员比白人驾驶员更有可能被拦截。
    ```
*   **TEACHER_PEFT:**
    ```
    该指导还指出，密苏里州总检察长办公室最近发布的一份报告表明，在该州黑人司机比白人司机被拦截的可能性高75%。
    ```
*   **STUDENT_PEFT:**
    ```
    该咨询还指出，由蒙大拿州主任办公室最近的报告表明，在该州驾驶的人中，黑人比白人更有可能被查到。
    ```
*   **HLKD:**
    ```
    该咨询也指向了由密苏里州 attorney general的办公室最近发表的一份报告，该报告显示在密苏里州行驶的黑人司机比白人司机更有可能被拦截。
    ```
*   **SLKD:**
    ```
    该报告还指出，最近的蒙代斯州律师机构的一项调查显示黑人驾驶员在该州被拉下的可能性比白人的高。
    ```

---

### Sample 13

**English:**
```
"The advisory is for people to be aware, and warn their families and friends and co-workers of what could happen in Missouri," Chapel said.
```

**Reference Chinese:**
```
查培尔说：“该份咨询是为了提高人们的意识，警告他们的家人、朋友和同事在密苏里州可能发生的情况。”
```

**Model Outputs:**
*   **TEACHER:**
    ```
    “警告人们要警觉，提醒家人、朋友和同事可能发生的事情。”——卡希尔说。
    ```
*   **STUDENT:**
    ```
    提示是提醒人们注意，让他们知道在密歇根州可能发生什么，包括他们的家人和朋友以及同事。
    ```
*   **TEACHER_PEFT:**
    ```
    “这是给人们一个警醒，让他们意识到在密苏里州会发生什么，并提醒他们的家人、朋友和同事。” 查兰说。
    ```
*   **STUDENT_PEFT:**
    ```
    该意见旨在让人们意识到并警告家人和朋友以及同事，他们可能会发生在美国密尔沃基市的什么情况。
    ```
*   **HLKD:**
    ```
    该咨询是提醒人们了解并告知家人、朋友和同事可能在蒙大拿州发生的什么。 檓柏说。
    ```
*   **SLKD:**
    ```
    这个报告旨在让人民知晓，他们家和朋友以及同事知道在马萨诸塞州发生什么情况。 他说道。
    ```

---

### Sample 14

**English:**
```
"People need to be ready, whether it's bringing bail money with them, or letting relatives know they are traveling through the state."
```

**Reference Chinese:**
```
“人们需要做好准备，无论是携带保释金前往密苏里州，还是让亲属知道自己在州内旅行”。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    人们需要准备好，无论是带着保释金，还是让亲戚知道他们正通过该州。
    ```
*   **STUDENT:**
    ```
    人们需要准备好，无论是带着押解钱还是让亲属知道他们正在通过州。
    ```
*   **TEACHER_PEFT:**
    ```
    人们需要准备，无论是带着保证金上路，还是让亲戚知道他们正在通过该州。
    ```
*   **STUDENT_PEFT:**
    ```
    人们需要准备，不管带着押解款还是让亲属知道他们正在通过国家。
    ```
*   **HLKD:**
    ```
    人们需要准备好，无论他们带的是押金还是让亲属知道他们是通过州旅行的。
    ```
*   **SLKD:**
    ```
    人们需要准备好，无论是把钱带走还是让亲属知道他们正在旅行。
    ```

---

### Sample 15

**English:**
```
Missouri recorded 100 hate crimes in 2015, according to the latest figures from the FBI's hate crime reporting program, ranking the state at 16th in the country in terms of the number of such violations.
```

**Reference Chinese:**
```
根据联邦调查局仇恨犯罪报告计划的最新数据，密苏里州在 2015 年记录了 100 起仇恨罪行；根据罪行量，该州在全国排名第 16 位。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    根据美国联邦调查局仇恨犯罪报告项目最新公布的数据，密苏里州2015年共记录了100起仇恨犯罪事件，位居全美第16位。
    ```
*   **STUDENT:**
    ```
    据美国联邦调查局（FBI）的仇恨犯罪报告程序最新统计数据，伊利诺伊州在2015年记录了100起仇恨犯罪。该州以16名第一名的身份排名全国，这是自2014年以来首次出现。
    ```
*   **TEACHER_PEFT:**
    ```
    根据联邦调查局的仇恨犯罪报告，密苏里州在2015年记录了100起仇恨犯罪，排在美国第16位。
    ```
*   **STUDENT_PEFT:**
    ```
    根据美国联邦调查局（FBI）的仇恨犯罪报告，该州在2015年记录了100起仇恨犯罪，排名全国第十六。
    ```
*   **HLKD:**
    ```
    2015年，孟菲斯（Missouri）记录了100起仇恨犯罪，根据美国联邦调查局的仇恨犯罪报告项目，该州排名为第16位，在全国范围内，仇恨犯罪的数量是最多的。
    ```
*   **SLKD:**
    ```
    根据美国联邦调查局的仇恨犯罪报告程序，2015年，马萨诸塞州记录了100个仇恨犯罪案件。 这些罪犯被列为该州在该地区排名第16位。
    ```

---

### Sample 16

**English:**
```
The travel warning is also a response to a new Missouri law that would make it more difficult to sue a business for housing or employment discrimination.
```

**Reference Chinese:**
```
旅行警告也是对密苏里州新法律的回应，该法律将使起诉住房或就业歧视企业变得更加困难。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    旅行警告也回应了密苏里州的一项新法律，该法律将使对商业提起针对住房或就业歧视的诉讼更难。
    ```
*   **STUDENT:**
    ```
    旅行警告也是针对新密州的法律，该法律将使起诉雇主或雇员对住房或就业歧视的诉讼更加困难。
    ```
*   **TEACHER_PEFT:**
    ```
    旅行警告也对密苏里州一项新的法律作出回应，这项法律会使得针对企业进行住房或就业歧视的诉讼更加困难。
    ```
*   **STUDENT_PEFT:**
    ```
    旅行警告也是对新一任马萨诸塞州法律，该法律会使得起诉企业进行住房或就业歧视的诉讼变得更加困难。
    ```
*   **HLKD:**
    ```
    旅行警告也是对新密州的法律，该法律将使起诉一家企业从事住房或就业歧视变得更加困难。
    ```
*   **SLKD:**
    ```
    旅行警告也是对新州法律的回应，该法律将使它更加难以起诉一个从事房屋或就业歧视的商业。
    ```

---

### Sample 17

**English:**
```
Previously, the American Civil Liberties Union (ACLU) had issued travel advisories for Texas and Arizona after the states passed immigration enforcement laws requiring local law enforcement to detain people on immigration violations which the ACLU said would increase racial profiling.
```

**Reference Chinese:**
```
此前，美国各州通过了移民执法法律，要求当地执法部门拘留移民违规人员，美国公民自由联盟 (ACLU) 表示此举会增加种族诉讼数量，并发布了针对德克萨斯州和亚利桑那州的旅行咨询。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    此前，美国公民自由联盟（ACLU）针对得克萨斯州和亚利桑那州通过的移民执法法案发布了旅行警告，该法案要求地方执法部门在移民违规行为上拘留人，并且称这些措施将增加种族歧视。
    ```
*   **STUDENT:**
    ```
    以前，美国公民自由联盟（ACLU）曾发布旅行警告，针对德克萨斯州和阿联酋，因为这两个州的法律要求当地执法机构在移民违规案件上拘留人，并且ACLU认为这会增加种族偏见。
    ```
*   **TEACHER_PEFT:**
    ```
    此前，美国公民自由联盟（ACLU）曾针对得克萨斯州和亚利桑那州发布过旅行警告，因为这两州通过了要求地方执法机构对违反移民法律的人进行拘留的移民执行法。 这些法案被 ACLU 认为会增加种族歧视。
    ```
*   **STUDENT_PEFT:**
    ```
    以前，美国公民自由联盟（ACLU）在移民执法要求本地执法当局将违法入境人员逮捕后就发布过旅行警告，而这些警报则声称会增加种族偏见。
    ```
*   **HLKD:**
    ```
    以前，美国公民自由联盟（ACLU ） 发布了针对加利福尼亚州和阿肯色州的旅行禁令，因为这两省通过要求当地执法机构拘留非法入境的人来实施移民执法措施。 ACLU 表示，这些措施将增加种族歧视。
    ```
*   **SLKD:**
    ```
    之前，美国公民自由联盟（Civil Liberties Union）曾发布了关于对移民进行强制检查的旅行指南，而该组织声称这将增加种族歧视。
    ```

---

### Sample 18

**English:**
```
Travel warnings are usually issued by the State Department for other countries, but lately, advocacy groups have resorted to the measure in response to certain laws and trends inside the US.
```

**Reference Chinese:**
```
旅行警告通常是由美国政府针对其他国家发布的，但最近，咨询团体采取这一方式以应对美国境内的某些法律和趋势。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    旅行警告通常由国务院向其他国家发出，但最近，倡导团体则在针对美国内部某些法律和趋势的情况下采取这种措施。
    ```
*   **STUDENT:**
    ```
    旅行警告通常由国务院外交部发出，但最近，一些倡导团体采取措施回应美国的一些法律和趋势。
    ```
*   **TEACHER_PEFT:**
    ```
    旅行警告通常由国务院对其他国家发布，但最近一些倡导组织则利用这一措施应对美国内部某些法律和趋势。
    ```
*   **STUDENT_PEFT:**
    ```
    旅行警告通常由其他国家的驻外机构发布，但最近，一些倡导组织为了应对美国某些法律和趋势而采取了这种措施。
    ```
*   **HLKD:**
    ```
    旅行警告通常由美国驻外使馆发布，但最近一些倡导组织也采取了这种措施以应对某些内部的法律和趋势。
    ```
*   **SLKD:**
    ```
    过去几年，游行警告通常由国家层面发出，但最近一些反对组织在应对美国某些法律和趋势的背景下采取了这一措施。
    ```

---

### Sample 19

**English:**
```
After experiencing the “golden era” of a soaring box office in 2015, the film market retreated into a cooling-off period in 2016. Whether box office takings could surpass last year’s total of RMB44.069 billion is questionable.
```

**Reference Chinese:**
```
经历2015年票房猛增的“黄金时代”后，2016年整体电影市场进入了冷静期，能否突破去年440.69亿元的总票房成绩都成为一个悬念。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    自2015年电影市场经历了一段票房大热时期之后，2016年电影市场的热度有所下降。今年的总票房是否能超过去年的440.69亿元人民币仍然是一个未知数。
    ```
*   **STUDENT:**
    ```
    在2015年的“黄金时期”，电影市场经历了一次“温饱期”，到2016年则进入了冷却期。票房能否超过去年的总额人民币44.069亿元，目前仍存在疑问。
    ```
*   **TEACHER_PEFT:**
    ```
    在2015年经历“票房狂潮”之后，电影市场进入了一段冷却期。 是否能够超过去年的总票房收入人民币440.69亿元仍然是个未知数。
    ```
*   **STUDENT_PEFT:**
    ```
    在2015年的“黄金时代 ” ， 影片市场经历了一次降温期，而票房收入是否能够超过去年的总值440.69亿美元也值得怀疑。
    ```
*   **HLKD:**
    ```
    在2015年狂热的票房时代之后，电影市场退回到冷却期。 虽然票房收入可能超过去年的总和人民币440.69亿元是否值得怀疑？
    ```
*   **SLKD:**
    ```
    在2015年一次辉煌的“黄金时期 ” 的后，电影市场在2016年的冷落期变得平滑。 该时期的箱票销售是否能超越去年总价值440.069亿元的人民币？
    ```

---

### Sample 20

**English:**
```
Data from the National Bureau of Statistics revealed that in October, prices of new and second-hand residential properties cooled, up 0.6% and 1.1% month-on-month, respectively.
```

**Reference Chinese:**
```
从国家统计局公布的数据看，10月，北京新房和二手房价格双双降温，环比仅上涨0.6%和1.1%。
```

**Model Outputs:**
*   **TEACHER:**
    ```
    国家统计局数据显示，10月新建和二手住宅价格环比分别下降了0.6%和1.1%。
    ```
*   **STUDENT:**
    ```
    在十月，新建和二手住宅的价格降温，上涨了0.6%，每月上涨了1.1%。
    ```
*   **TEACHER_PEFT:**
    ```
    国家统计局的数据显示，10月份新和二手住宅价格分别下降0.6 % 和1.1 % 。
    ```
*   **STUDENT_PEFT:**
    ```
    国家统计局数据显示，十月新旧住宅的价格都出现了降温，月度变化分别为0.6 % 和 1.1 % 。
    ```
*   **HLKD:**
    ```
    国家统计局的数据显示，十月新和二手住宅价格降温，其中新住宅价格上涨了0.6 % ， 新房下降了1.1 % 。
    ```
*   **SLKD:**
    ```
    国家统计局数据显示，10月新和第二手住宅房价下降了0.6 % ， 以及1.1 % 。
    ```

---

## Overall Model Scores (BERTScore)

### TEACHER
*   **Average F1:** 0.8181
*   **Average Precision:** 0.8214
*   **Average Recall:** 0.8161

### STUDENT
*   **Average F1:** 0.7812
*   **Average Precision:** 0.7862
*   **Average Recall:** 0.7775

### TEACHER_PEFT
*   **Average F1:** 0.8290
*   **Average Precision:** 0.8272
*   **Average Recall:** 0.8318

### STUDENT_PEFT
*   **Average F1:** 0.7910
*   **Average Precision:** 0.7986
*   **Average Recall:** 0.7844

### HLKD
*   **Average F1:** 0.7918
*   **Average Precision:** 0.7944
*   **Average Recall:** 0.7900

### SLKD
*   **Average F1:** 0.7720
*   **Average Precision:** 0.7869
*   **Average Recall:** 0.7594

