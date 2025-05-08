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
    上周，古装剧《甄嬛传》的播出临时中断，意外引发了关于本土自制剧虚假收视率的激烈讨论。
    ```
*   **STUDENT:**
    ```
    上个星期，播出的电视剧《私人厨房》暂停播放，因为意外触发了关于本地剧集虚假评分的 heated debate。
    ```
*   **TEACHER_PEFT:**
    ```
    上一周，由于“私厨 ” （ Beauty Private Kitchen）的播出暂时被中断，以及该电视剧意外引发关于本地电视剧虚假评级的激烈争论。
    ```
*   **STUDENT_PEFT:**
    ```
    上周，因本地电视剧《美丽私人厨房》的播出而暂时中断，还引发了一场关于本地剧作受欢迎程度的争论。
    ```
*   **HLKD:**
    ```
    上周，由女厨女郎主持的《美丽私人厨房》节目暂时停播，并且意外引发了关于本地制作的电视剧被虚假评分所引起的激烈讨论。
    ```
*   **SLKD:**
    ```
    上周，由《私人厨房》（Private Kitchen）播出的节目被暂时中断，并因此引发了对本地制作的剧集虚假评分的激烈争论。
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
    公民权利团体发布密苏里州旅行警告
    ```
*   **STUDENT:**
    ```
    民权团体发出旅行警告，要求勿前往密苏里州
    ```
*   **TEACHER_PEFT:**
    ```
    公民权利团体发布密苏里州旅行警告
    ```
*   **STUDENT_PEFT:**
    ```
    公民权组织发布警告，要求马萨诸塞州旅游。
    ```
*   **HLKD:**
    ```
    民权组织警告墨西哥旅行者
    ```
*   **SLKD:**
    ```
    民权组织发出警告，要求马萨诸塞州旅行。
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
    全国有色人种协进会发布了一则警示，提醒有色人种旅客因为密苏里州的歧视性政策和种族攻击而前往该地区。
    ```
*   **STUDENT:**
    ```
    黑人活动家国家非洲裔大陆联盟发布了一份警告，因为该州的歧视政策和种族攻击导致人们前往孟加拉国旅行。
    ```
*   **TEACHER_PEFT:**
    ```
    因为密苏里州歧视性的政策和种族仇恨攻击，全国有色人种促进会发布警告，提醒他们不要前往该州。
    ```
*   **STUDENT_PEFT:**
    ```
    全国有色运动协会发布警告，因为因为州的歧视政策和暴力袭击，黑人旅行到马萨诸塞州是因为危险。
    ```
*   **HLKD:**
    ```
    全国黑人进步协会发布了关于那些来自孟加拉国的有色人的游行警报，因为该省歧视黑人和攻击者。
    ```
*   **SLKD:**
    ```
    美国有色人种协会发布了关于因孟萨克州的歧视性政策和种族攻击而前往该州旅行的人的警报。
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
    美国全国有色人种协进会（NAACP）对于密苏里州的旅行警示，自2017年8月28日生效，提醒所有非洲裔旅客、游客和密苏里州居民在当前全州发生的一系列有争议且基于种族事件的情况下，应特别注意并采取极端谨慎措施。该组织声明如下。
    ```
*   **STUDENT:**
    ```
    美国非洲裔旅行咨询小组（NAACP）针对俄亥俄州的旅行建议，自2017年8月28日起生效，强调了在该州旅行时对所有种族背景的人士和俄亥俄居民保持特别关注，并且要采取极端谨慎的态度。根据NAACP的声明，这些团体表示：“鉴于近期在俄亥俄州发生的系列不道德、基于种族的事件，以及在此期间所发生的一切，我们呼吁所有种族背景的人士和俄亥俄居民都应格外小心地旅行。”
    ```
*   **TEACHER_PEFT:**
    ```
    “密苏里州旅行警告（The NAACP Statewide Travel Advisory） ， ” 有效期至2017年8月28日，要求密苏里州的非洲裔美国人、游客和居民在全州最近发生的一系列可疑基于种族事件发生期间格外注意，特别是在堪萨斯城发生的几起案件中出现的一些反犹太言论。
    ```
*   **STUDENT_PEFT:**
    ```
    该安纳巴克州旅行咨询委员会（NAACP Travel Advisory for the State of Missouri）于2017年8月28日生效，它要求非洲裔旅者、游客和蒙大拿州居民在该省旅行时要格外注意并当采取极端的警戒措施。 它们指出，近期该省出现了一些令人不安的黑人袭击事件，这些事件发生在该省大部分地区，它们还提到，在该省中部地区发生的一些非常可疑的种族冲突事件，以及在其中活动的警察对此进行了警告。
    ```
*   **HLKD:**
    ```
    “纳瓦亚大陆旅行顾问委员会”于2017年8月28日生效的旅游咨询建议指出，对来自美国南部的非洲裔旅者、游客和蒙大拿州的旅客支付特别关注，并且在他们旅行期间要格外小心地遵守有关黑人犯罪行为发生在我省的所有地方的系列可疑事件。
    ```
*   **SLKD:**
    ```
    美国南卡罗来纳州旅行咨询委员会（NAACP）对2017年8月28日生效的建议称，非洲裔美国人、访客和蒙大拿人要格外注意在该州旅行，并且考虑到最近发生的一些疑虑性种族事件，以及其中所提到的相关信息。
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
    最近，密苏里州通过了一项法律，使得人们在赢得歧视诉讼方面变得更加困难，并且该州的执法部门对少数族裔进行了过度的打击，这导致了这个团体发布了旅行警报，美国全国有色人种协进会说。
    ```
*   **STUDENT:**
    ```
    一个最近的马萨诸塞州法律，使人们更容易赢得歧视诉讼，并且该州执法部门对少数族裔群体采取过激措施，引起了团体发出旅行警告。据美国非裔权利协会（NAACP）称。
    ```
*   **TEACHER_PEFT:**
    ```
    最近出台的一条密苏里州法律以及该州执法部门对少数族人过分偏见的法律促使了民权联盟发布旅行警报。
    ```
*   **STUDENT_PEFT:**
    ```
    最近的一部蒙大拿州法律加重了人们对歧视诉讼的抵抗，同时也加重了州内警察对少数群体的偏见，因此该团体发布警告书，告之曰：“ 多少有人能够赢得歧视诉讼。 ” 这是纳瓦克联盟发出的警告信号。
    ```
*   **HLKD:**
    ```
    最近的马萨诸塞州法律令人们难以获得歧视诉讼，同时该省的执法法对少数民族群体进行过多限制，引起了NAACP集团发布旅行警报。
    ```
*   **SLKD:**
    ```
    最近，俄勒冈州的法律使得人们更容易获得歧视诉讼，而该州执法部门对少数族裔进行偏袒也引起了美国非裔团体发出警告。
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
    你有人权侵害的事情正在发生。
    ```
*   **STUDENT:**
    ```
    你正在侵犯人们的民权。
    ```
*   **TEACHER_PEFT:**
    ```
    "你有违反民权的行为发生在人民身上。
    ```
*   **STUDENT_PEFT:**
    ```
    你违反了公民权利。
    ```
*   **HLKD:**
    ```
    “人们在非法行为中受到侵害。
    ```
*   **SLKD:**
    ```
    你正在侵犯人的民权。
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
    因为他们肤色，他们被拦截检查，被打伤或被杀，“密苏里州黑人民权委员会主席罗德·查尔 chapel 对《堪萨斯城星报》说。
    ```
*   **STUDENT:**
    ```
    他们被拦截是因为他们的肤色，他们被打或杀死，“美国孟菲斯纳塞党主席罗伯特·查普顿”表示《堪萨斯城星报》。
    ```
*   **TEACHER_PEFT:**
    ```
    他们因为肤色而被拦截，遭到殴打甚至杀害。 " 美国密苏里州黑人权利委员会主席罗布·查佩尔告诉《圣劳伦斯纪事报 》 。
    ```
*   **STUDENT_PEFT:**
    ```
    他们是因为肤色而受到迫害，遭到殴打或杀害的纳粹党领袖罗伯特·普莱姆（Rod Chapel）在《堪萨斯州纳粹主义党》报中表示。
    ```
*   **HLKD:**
    ```
    他们被皮肤颜色的不同所吸引，有时受到伤害或遭到杀害，因此这些人们受到了外界的排斥。
    ```
*   **SLKD:**
    ```
    他们被贴上肤色的标签，被打、被击毙，“ 比利·克劳普总统”告诉《卡斯蒂拉星报》说。
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
    我们听到的抱怨比以前任何时候都要多。
    ```
*   **STUDENT:**
    ```
    我们听到抱怨的数量远远超过了我们以前听来的数量。
    ```
*   **TEACHER_PEFT:**
    ```
    "我们以前从未听到过这样的抱怨。
    ```
*   **STUDENT_PEFT:**
    ```
    我们已经听到了之前未曾听到的抱怨。
    ```
*   **HLKD:**
    ```
    我们听说这方面的投诉数量和频率与以往相比要增加不少。
    ```
*   **SLKD:**
    ```
    我们听到的投诉数量比以往要多。
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
    这是美国州政府首次发布的此类警告。
    ```
*   **STUDENT:**
    ```
    这是该组织首次发出的有关美国一国的情况的警告。
    ```
*   **TEACHER_PEFT:**
    ```
    这是组织对美国境内某州发布的第一份警告。
    ```
*   **STUDENT_PEFT:**
    ```
    这是组织首次向美国国家发布的一份警告信。
    ```
*   **HLKD:**
    ```
    这是美国第一份有关该组织的警告。
    ```
*   **SLKD:**
    ```
    这是美国组织首次发出关于国家的警告。
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
    该团体列举了种族侮辱黑学生事件，以及田纳西州28岁的黑人男子托比·桑德斯的死亡。
    ```
*   **STUDENT:**
    ```
    这所大学的社团引用了诸如黑学生种族歧视言论之类的事件，以及Tennessee州立大学28岁的黑人男子Tory Sanders的死亡。
    ```
*   **TEACHER_PEFT:**
    ```
    该组织列举的事件包括密西根大学种族污蔑黑人学生、田纳辛州28岁的Tory Sanders死亡。
    ```
*   **STUDENT_PEFT:**
    ```
    该联盟引用了包括在蒙大拿大学和死于特兰蒂斯的黑人男子所发生的种族骚扰事件。
    ```
*   **HLKD:**
    ```
    该团体指出，大学里黑人学生遭受的种族歧视、28岁的黑人学生泰勒·萨特尔（Tory Sanders）被杀害。
    ```
*   **SLKD:**
    ```
    该小组引用了如大学米萨克尔学院（University of Missouri）的种族歧视言论以及28岁的黑人男子泰罗·斯兰德（Tory Sanders）死亡事件。
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
    桑德斯先生今年早些时候在旅行途中因燃料耗尽而死亡，他的死因存在疑问。当时他被莫瑞州的警察逮捕，但并未因犯罪指控被捕。
    ```
*   **STUDENT:**
    ```
     Sanders 死亡的情况当时可能不被证实，他在行驶过程中因为没有足够的汽油而走失，并被墨西河州警察带走，未被指控任何犯罪。
    ```
*   **TEACHER_PEFT:**
    ```
    桑德斯在本月初因行驶里程耗尽而身亡，当时他被路易斯安那州警察无罪拘留。
    ```
*   **STUDENT_PEFT:**
    ```
    桑德斯在去年夏天驾车经过伊利诺斯州时感到气喘吁尽，被一名警察带入了牢里，而该警官则以涉嫌盗窃罪为由被逮捕。
    ```
*   **HLKD:**
    ```
    桑德斯今年早些时候因为途经蒙大拿时燃尽了油箱，而无法继续行驶，被密安州警方带走。 罗萨尔没有犯罪的嫌疑。
    ```
*   **SLKD:**
    ```
     Sanders在去年去世，当时他正在旅行，途中因用尽了汽油而无法继续前行，因此被美国马萨诸塞州警察逮捕，并未被指控有任何犯罪行为。
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
    该指南也指出，密苏里州司法部长办公室最近发布的一项报告称，在该州的黑人司机比白人司机被拦下的可能性高75%。
    ```
*   **STUDENT:**
    ```
    这个咨询也指出，根据密苏里州律师办公室最近的报告，该州黑人司机比白人司机更有可能被检查。
    ```
*   **TEACHER_PEFT:**
    ```
    该咨询还指出，密苏里州总检察长最近的一份报告表明，在该州驾车的黑人是白人的75%更有可能被拦截。
    ```
*   **STUDENT_PEFT:**
    ```
    该报告指出，美国蒙大拿州 attorney general office recently released a study showing that black drivers in the state were 75% more likely to be stopped and arrested than white drivers.
    ```
*   **HLKD:**
    ```
    该咨询委员会还指出，州司法厅最近发布的黑人驾车率调查数据显示，比白人要高出75 % 。
    ```
*   **SLKD:**
    ```
    该咨询委员会还指出，最近由蒙大拿州 attorney general办公室发布的报告显示，在该州行驶的黑人驾驶员比白人驾驶员更有可能被警察拦下。
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
    “此咨询提醒人们要意识到可能发生的情况，并告知家人、朋友和同事。”
    ```
*   **STUDENT:**
    ```
    “咨询是提醒人们要警惕，特别是他们的家人和朋友、同事可能会发生的什么。”，Chapel说道。
    ```
*   **TEACHER_PEFT:**
    ```
    “这个咨询是让人们能够意识到问题，并警告他们的家人、朋友和同事可能发生的事件。
    ```
*   **STUDENT_PEFT:**
    ```
    该警告适用于人们能够意识到的事情，而且也警告他们的家人、朋友和同事有关会发生什么情况的警告。
    ```
*   **HLKD:**
    ```
    “这份咨询面向公众，是告知人们在密尔沃斯会发生什么情况，并告诫家人、朋友和同事以及雇主们。
    ```
*   **SLKD:**
    ```
    “这份建议是提醒人们要意识到在密苏里州发生的事情，以及告诉家人、朋友和同事会发生什么。” 佩尔特说。
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
    人们需要准备好，无论是带钱出来交保释金，还是让亲戚知道他们正在州内旅行。
    ```
*   **STUDENT:**
    ```
    人们需要准备好，无论他们带着什么钱，还是让亲属知道他们是经过州的。
    ```
*   **TEACHER_PEFT:**
    ```
    无论携带 bail 资金，还是让亲戚知道他们正在穿越该州，人们都需要做好准备。
    ```
*   **STUDENT_PEFT:**
    ```
    无论他们带了多少钱，人们都需要准备好。
    ```
*   **HLKD:**
    ```
    人们需要准备，无论是在带来担保的条件下还是让亲属知道他们正在旅行时都需携带现金。
    ```
*   **SLKD:**
    ```
    人们需要准备好，无论是将押解款带去还是让亲属知道他们通过国家进入。
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
    根据美国联邦调查局（FBI）的仇恨犯罪报告项目最新数据，密苏里州在2015年记录了100起仇恨犯罪，位居全国第16位，在这一类违法行为中。
    ```
*   **STUDENT:**
    ```
    根据美国联邦调查局的仇恨犯罪报告系统，密苏里州在2015年记录了100起仇恨犯罪，排名全国第16位。
    ```
*   **TEACHER_PEFT:**
    ```
    2015年，密苏里州记录了100起仇恨犯罪，最新数据显示该州的仇恨犯罪数量在全国排第16位。
    ```
*   **STUDENT_PEFT:**
    ```
    根据美国联邦安全局的胡适犯罪报告项目最新统计，2015年墨西哥共发生100起仇恨案件，位列全国十大罪犯州之列。
    ```
*   **HLKD:**
    ```
    俄蒙州2015年记录了100起仇恨犯罪，据美国联邦调查局的仇恨犯罪报告程序最新统计，该州排在全国第16名。
    ```
*   **SLKD:**
    ```
    2015年，孟沙尔州记录了100起仇恨犯罪，这是美国全国调查局（FBI） Hate Crime Reporting Program最新发布的数据，该报告排名孟沙尔州为美国第16名。
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
    旅行警告也是对新密苏里州法律的回应，该法律将使在住房或就业歧视方面起诉商业变得更加困难。
    ```
*   **STUDENT:**
    ```
    旅行警告也是针对新密州的一条新的密省法律，这条法律将使起诉商业机构对住房或就业歧视的诉讼变得更加困难。
    ```
*   **TEACHER_PEFT:**
    ```
    旅行警告也是对密苏里州即将出台的一项新法律的响应，该新法律将使得企业因住房或就业歧视提起诉讼更加困难。
    ```
*   **STUDENT_PEFT:**
    ```
    旅行警告只是对一个新的马萨诸塞州法律的回应，该法律将令企业更难为住房或就业歧视提供索赔服务。
    ```
*   **HLKD:**
    ```
    旅行警告也是应对新颁布的《马萨诸塞州房屋和就业歧视法》这一新的法律所引发的新举措。
    ```
*   **SLKD:**
    ```
    旅行警告也是对新一届马萨诸塞州立法机构通过的新法案，该法案将使企业更容易提起住房或就业歧视诉讼。
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
    此前，美国公民自由联盟（ACLU）曾针对得克萨斯州和亚利桑那州发布旅行警告，在这些州通过了要求地方执法部门拘捕违反移民法律的人的移民执法法案，而 ACLU 表示这将加剧种族歧视。
    ```
*   **STUDENT:**
    ```
    以前，美国公民自由联盟（ACLU）曾发布过对加利福尼亚州和阿联酋的旅行警告，因为这两个州通过实施移民执法法律要求当地执法机构拘留那些违反移民规定的人员，而ACLU认为这将增加种族偏见。
    ```
*   **TEACHER_PEFT:**
    ```
    此前，美国公民自由联盟曾发布过关于德克萨斯州和亚利桑那州的旅行警告，因为两州通过了要求当地执法部门在移民违规事件中逮捕当事人的移民执法法案。 该法案引发了 ACLU的担忧，认为这会增加警官随意搜查犯人。
    ```
*   **STUDENT_PEFT:**
    ```
    此前，美国公民自由联盟（ACLU）在经过要求当地司法机关采取拘留措施的州通过移民检查要求后发布了针对德克萨斯州和阿肯奇州的旅行警告。 该联盟声称这将增加执法活动的种族化。
    ```
*   **HLKD:**
    ```
    此前，美国公民自由联盟（ACLU）发布了针对加州和阿萨提的旅行指南后要求当地执法部门对移民违规人员进行逮捕。 ACLU认为这样做会加大警方的歧视力度，从而引发抗议活动。
    ```
*   **SLKD:**
    ```
    此前，美国公民自由联盟（ACLU）在2014年对加利福尼亚州和阿肯色州实施旅行警示后，要求当地执法部门将移民违法行为人员拘留。 ACLU认为这些措施会增加种族歧视行为。
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
    旅行警告通常由国务院针对其他国家发布，但最近，倡导团体则在应对美国内部某些法律和趋势时采取这一措施。
    ```
*   **STUDENT:**
    ```
    旅行警告通常由美国政府的国务卿或其他国家官员发出，但最近，一些倡导者采取了措施来应对在美国内的一些法律和趋势。
    ```
*   **TEACHER_PEFT:**
    ```
    旅行警告通常是由美国国务院或其他国家的政府发布的，但现在一些倡导团体在某些国内法律和趋势面前开始采取这样的措施。
    ```
*   **STUDENT_PEFT:**
    ```
    各国旅行警告通常由国家部发布，但在最近一段时间中，倡导组织为了某些美国法律和趋势而采取的措施。
    ```
*   **HLKD:**
    ```
    国家安全委员会通常会发出旅行警告，但最近一些倡导组织开始利用这一措施来应对美国某些法律和趋势。
    ```
*   **SLKD:**
    ```
    旅行警告通常由美国国家部发布，但最近一些倡导组织为了应对某些在美国内发生的法律和趋势而采取了这一措施。
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
    2015年电影市场经历了“黄金时代”，票房收入激增，达到了RMB440.69亿元。然而，在2016年，电影市场似乎进入了冷却期，票房收入能否超过去年的总额仍有待观察。
    ```
*   **STUDENT:**
    ```
    电影市场在2015年的“黄金时代”后，在2016年出现了降温期。票房能否超越去年的总收入人民币44.069亿元存在疑问。
    ```
*   **TEACHER_PEFT:**
    ```
    在经历“黄金时代”大受追捧的电影市场后，2016年该领域再度进入了一个冷却期。 是否能够超过去年创下的RMB440.69亿美元总票房纪录值得怀疑。
    ```
*   **STUDENT_PEFT:**
    ```
    在2015年繁荣的BOXOSS市场后，电影市场的冷却期出现在2016年。
    ```
*   **HLKD:**
    ```
    2015年电影市场的“黄金时代 ” ， 然而该市场在2016年又迎来了降温期，这使得去年的票房总额达到RMB4,406.9亿美元。 虽然票房能超过去年，但票房增幅仍然只有约3%。
    ```
*   **SLKD:**
    ```
    在2015年票房大爆发的“黄金时期 ” ， 市场开始进入冷却期。 如果票房收入能超过去年的总额440.69亿元，那么这将是一个值得怀疑的迹象。
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
    国家统计局的数据表明，10月份新建和二手房的价格均有所降温，分别环比上涨了0.6%和1.1%。
    ```
*   **STUDENT:**
    ```
    据国家统计局的数据，十月新和二手住宅价格降温，下降了0.6%，上涨了1.1%。
    ```
*   **TEACHER_PEFT:**
    ```
    国家统计局数据显示，10月份，新和二手住宅价格分别下降了0.6 % 和 1.1 % 。
    ```
*   **STUDENT_PEFT:**
    ```
    由国家统计局公布的数据显示，10月份新和二手住宅价格分别下降了0.6 % 和1.1 % ， 这表明10月份新旧住宅价格出现了降温。
    ```
*   **HLKD:**
    ```
    从国家统计局的数据看，10月份新和二手房价格出现了降温，同比涨幅为0.6 % 和 1.1 % 。
    ```
*   **SLKD:**
    ```
    国家统计局数据显示，十月新和第二手住宅价格在月度上出现了下降，分别下降了0.6 % 和1.1 % 。
    ```

---

## Overall Model Scores (BERTScore)

### TEACHER
*   **Average F1:** 0.8355
*   **Average Precision:** 0.8384
*   **Average Recall:** 0.8334

### STUDENT
*   **Average F1:** 0.7946
*   **Average Precision:** 0.7990
*   **Average Recall:** 0.7912

### TEACHER_PEFT
*   **Average F1:** 0.8148
*   **Average Precision:** 0.8229
*   **Average Recall:** 0.8077

### STUDENT_PEFT
*   **Average F1:** 0.7551
*   **Average Precision:** 0.7631
*   **Average Recall:** 0.7490

### HLKD
*   **Average F1:** 0.7662
*   **Average Precision:** 0.7763
*   **Average Recall:** 0.7573

### SLKD
*   **Average F1:** 0.7803
*   **Average Precision:** 0.7848
*   **Average Recall:** 0.7766

