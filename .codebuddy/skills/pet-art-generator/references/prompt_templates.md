# 灵兽秘境敌人 — AI 生图提示词（左右合成版）

> 每只宠物生成 **2 张图**（普通形态 + 觉醒形态），每张图为 **2:1 横版**，左半为头像、右半为全身战斗像，后续剪裁拆分使用。
> 来源参考：`/Users/huyi/rosa_games/fangzhi/宠物美术资源提示词v3.md`
> 画风对齐：与本游戏现有三星宠物头像（水墨国风 + 工笔重彩 Q 版）保持一致

---

## 一、画风定位

**核心风格**：中国传统水墨画 + 工笔重彩 Q 版（chibi / super deformed）

与本游戏现有三星宠物头像画风一致：
- **线条**：毛笔书法式墨线描边，有粗细变化、起收笔锋（非均匀卡通描边）
- **填色**：水墨晕染质感，允许同色系内淡墨渐晕，体现体积感与立体感
- **比例**：Q 版大头小身（头身比 2:1），保留萌感的同时具备仙侠气韵
- **配色**：中国传统矿物颜料色（朱砂红、石青蓝、石绿、赭石黄、墨色浓淡）
- **美学**：中国仙侠神话，**非西幻**、**非写实**、**非 3D**

**头像 vs 全身像的一致性要求**：
- 两侧角色必须是**同一只**，设计、配色、装饰、饰品完全相同
- 左侧头像：大头 + 肩部特写（头部≥65%画面），安静或微动态表情
- 右侧全身像：完整身体，带有战斗姿态（低伏、扑击、咆哮等），但**不删减任何原有装饰和饰品**
- 全身像仅在姿态上体现"战斗感"，角色本身的外观细节与头像保持一致

**抠图约束**：
- 必须有清晰的黑色墨线描边轮廓（毛笔风格，有粗细变化）
- 描边外侧不得有白色描边/光晕/颜色溢出
- 黑色墨线即为最外层边界，直接接触背景
- 禁止模糊、辉光、半透明羽化、写实光影等边缘模糊效果

---

## 二、图片规格

| 项目 | 规格 |
|------|------|
| 宽高比 | **2:1 横版**（如 1024×512 px） |
| 布局 | 左半 = 头像特写，右半 = 全身战斗像 |
| 背景 | 纯浅灰色 `#E0E0E0`，覆盖整张画布 |
| 格式 | PNG |
| 每只宠物 | 2 张（普通形态 1 张 + 觉醒形态 1 张） |
| 后续处理 | 沿中线剪裁为 2 张正方形图（头像 + 全身） |

---

## 三、通用提示词模板

### 普通形态模板

> 使用方式：将 `{角色描述}` 替换为下方各宠物的角色特征描述

```
A single 2:1 landscape image split into two equal halves on one canvas, solid plain single-color background light gray #E0E0E0 across the entire image. Both halves depict the EXACT SAME character with identical design, colors, markings, and accessories — only the framing differs.

LEFT HALF — AVATAR: chibi 2D Chinese ink wash painting style, super deformed cute, big head small body ratio 2:1, close-up of oversized head and upper shoulders filling the left half, expressive ink-painted eyes with reflective highlights.

RIGHT HALF — FULL BODY: the exact same character shown in full body view, front-facing, in a battle-ready combat stance (crouching, pouncing, roaring, or charging), the character fills 70-80% of the right half height. The full body retains ALL decorations, accessories, and design details from the avatar — nothing is removed, only battle posture is added.

UNIFIED STYLE FOR BOTH HALVES: Chinese calligraphy brush-style black ink outlines with varying thickness and expressive brush stroke feel, ink wash coloring with subtle tonal gradation and soft layered shading creating gentle volume and depth, light and shadow through ink density variation — lighter wash on highlights and denser ink in recessed areas, rich color palette mixing traditional Chinese mineral pigments with natural animal tones, Chinese Xianxia mythology aesthetic, NOT Western fantasy, NOT realistic, NOT 3D rendered, clean sharp ink-line edges for easy cutout.

STRICTLY FORBIDDEN: any text, letters, words, writing, watermark, runes, symbols, glyphs, seals, calligraphy marks. STRICTLY FORBIDDEN: white outline outside black ink outlines, white border, white edge glow, white halo, any fringe between outline and background. Also forbidden: glow effects, blur, soft edges, lighting effects. STRICTLY FORBIDDEN: humanoid form, human face, human body. This creature MUST be an ANIMAL or BEAST.

This is the NORMAL base form (not evolved). {角色描述}
```

### 觉醒形态模板

> 与普通形态模板相同的前缀，仅将最后一段替换为：

```
（前缀同上……）

This is the AWAKENED max-star evolved form — more refined details, ornate accessories, golden star-rank accents on key accessories, more intense battle expression, more elaborate decorations than base version. {角色描述}
```

---

## 四、角色描述（33 只）

> 每只宠物提供**普通形态**和**觉醒形态**两段描述，分别插入上述对应模板的 `{角色描述}` 位置。

---

### #1 岩獾 (rock_badger) — R · 土 · 1-1

**普通形态**：
```
A young badger spirit with dark brown and sandy-cream fur with rocky plate-like patterns on the back and shoulders, a broad flat head with strong jaw, small sturdy legs with thick claws, large round amber-gold eyes with a stubborn grumpy expression, stone-textured stripe running from nose to tail, short bristly tail, a tiny amber bead on a thin cord around the neck, ink wash brush texture showing volume through tonal shading. FULL BODY BATTLE POSE: low crouching defensive stance with claws dug into the ground, head lowered showing the rocky back plates, fierce determined expression.
```

**觉醒形态**：
```
A majestic evolved badger spirit with deep bronze and obsidian-black fur with glowing amber-gold crack patterns across stone-armored back, large blazing topaz-gold eyes with an amber ring, golden metal claw-caps, ornate amber crystal on a chain at the neck, thicker stone plates with golden veining, flowing ink wash texture with rich tonal depth. FULL BODY BATTLE POSE: powerful charging attack with head lowered like a battering ram, stone plates glowing with golden cracks, unstoppable force expression.
```

---

### #2 炎狐 (flame_fox) — R · 火 · 1-2 波1

**普通形态**：
```
A young fox spirit kit with warm cream and soft peach body fur with ink wash brush texture, bright amber-orange ear tips fading from the cream base, a small fluffy tail with the very tip glowing ember-orange suggesting warmth, large sparkling teal-green eyes with a curious lively expression, tiny coral-red silk ribbon tied in a bow at the neck, rosy pink inner ears, subtle warm shadow under the chin giving roundness. FULL BODY BATTLE POSE: front paws spread in a low combat stance ready to pounce, body slightly crouched and leaning forward, mouth slightly open showing tiny fangs in a fierce cute growl, tail raised high with tip glowing ember-orange.
```

**觉醒形态**：
```
A majestic young fox spirit in evolved form with luxurious cream-white and warm amber fur with flowing ink wash texture, vivid golden-orange flame patterns along the cheeks like elegant war paint, large blazing teal-green eyes with a golden star-shaped ring in the pupil, pointed ears tipped with fiery vermilion-red and adorned with tiny golden bell earrings, an ornate small red jade pendant with golden filigree hanging at the neck on a crimson braided cord, bushy dual tails with brilliant sunset-orange and vermilion tips. FULL BODY BATTLE POSE: dynamic leaping attack with one front paw swiping forward showing tiny claws, body twisting mid-strike with powerful momentum, mouth open in a battle cry showing fangs, dual tails fanned out like twin flames.
```

---

### #3 焰狮 (blaze_lion) — SR · 火 · 1-2 波2

**普通形态**：
```
A young lion cub spirit with warm cream and soft peach body, rich golden-amber and deep crimson mane-fur with flame-shaped mane strands, large fierce golden eyes with inner fire glow, small rounded ears with fiery orange inner coloring, broad paws with warmth-glow, a fluffy tail with a flame-like tip, regal proud expression, a tiny ruby bead on a thin cord around the neck, ink wash brush texture showing volume. FULL BODY BATTLE POSE: standing tall with chest puffed out and mane blazing, one paw raised in a commanding roar pose, mouth open showing teeth, king-of-beasts pride.
```

**觉醒形态**：
```
A majestic evolved lion with magnificent golden-white and blazing vermilion mane with living flame tendrils, large blazing white-gold eyes with a flame ring, ornate golden crown-circlet with a tiny ruby, golden mane ornaments, dual fiery tail tips, regal imperial warrior form, an ornate ruby pendant in golden filigree on a silk cord, flowing ink wash with rich tonal depth. FULL BODY BATTLE POSE: devastating roar-attack with mane erupting in flames, body surging forward with royal fury, golden fire energy radiating, supreme lion king expression.
```

---

### #4 泡泡鱼 (bubble_fish) — R · 水 · 1-3 波1

**普通形态**：
```
A young pufferfish spirit with soft round turquoise-blue and cream body with translucent bubble-like spots, a chubby round body shape with tiny fins, large round bright aqua-blue eyes with a cheerful bubbly expression, small pursed mouth blowing tiny bubbles, translucent fin edges, a tiny sapphire bead on a thin cord, ink wash brush texture with soft tonal shading. FULL BODY BATTLE POSE: puffed up in defensive mode with spines slightly extended, body round and ready to launch a bubble barrage, determined cute expression.
```

**觉醒形态**：
```
A majestic evolved pufferfish spirit with shimmering pearl-blue and golden-turquoise body with luminous bubble patterns, large blazing sapphire eyes with a golden ring, ornate golden fin-crown, translucent golden-edged fins, golden bubble patterns across the body, an ornate sapphire pendant in golden filigree, flowing ink wash with rich oceanic depth. FULL BODY BATTLE POSE: fully puffed up with golden spines extended, surrounded by golden bubble energy, commanding ocean-spirit expression.
```

---

### #5 碧潮鲸 (tide_whale) — SR · 水 · 1-3 波2

**普通形态**：
```
A young whale spirit with smooth deep navy-blue body and white belly in ink wash, large wise dark eyes with a calm deep expression, subtle water-mist spray from blowhole, barnacle-like spots with blue crystal accents on the chin, broad fins with teal-blue edges, a tiny sapphire bead on a thin cord around the neck, gentle majestic ocean presence. FULL BODY BATTLE POSE: body surging forward through water energy, fins spread wide in a powerful dive, mouth partially open showing baleen, commanding ocean guardian expression.
```

**觉醒形态**：
```
A majestic evolved whale spirit with magnificent dark sapphire and golden-veined body in bold ink wash, large blazing deep-blue eyes with golden rings, ornate golden barnacle-crown formations, golden mist spray, magnificent golden-edged fins, golden ocean-rune markings along the body, an ornate sapphire pendant in golden filigree. FULL BODY BATTLE POSE: creating a massive tidal wave surge, body radiating ocean power, golden water-spirit energy, supreme sea guardian expression.
```

---

### #6 铁甲犰狳 (iron_armadillo) — R · 土 · 1-4 波1

**普通形态**：
```
A young armadillo spirit with iron-gray and steel-blue segmented shell plates with metallic sheen, a round compact body, large round gentle silver eyes with a calm sleepy expression, tiny clawed feet poking out from under the armor, a segmented tail with a metallic ball tip, small pointed ears barely visible between plates, a tiny amber bead on a thin cord around the neck, ink wash brush texture. FULL BODY BATTLE POSE: curled into an armored ball mid-roll, metallic plates gleaming, rolling forward as a living cannonball, stoic determined expression.
```

**觉醒形态**：
```
A majestic evolved armadillo spirit with magnificent polished dark-iron and golden-steel shell plates with glowing amber crack patterns, large blazing silver-gold eyes with an amber ring, ornate golden plate-edges, golden claw-tips, amber crystal formations along the spine, an ornate amber pendant in golden filigree on a silk cord, flowing ink wash with metallic depth. FULL BODY BATTLE POSE: unfolding from a devastating spin-attack with golden-edged plates flared outward, golden earth energy radiating, supreme iron fortress expression.
```

---

### #7 雷貂 (thunder_marten) — R · 雷 · 1-4 波2

**普通形态**：
```
A young marten spirit with dark chocolate-brown and cream-yellow fur with black jagged lightning-bolt stripes, a sleek elongated body with bushy tail, large round electric-yellow eyes with a sharp alert expression, tiny sparking whiskers, pointed ears with yellow inner coloring, small bright sparks visible on the fur tips, a tiny citrine bead on a thin cord around the neck, ink wash brush texture with electrified tonal shading. FULL BODY BATTLE POSE: arched back with fur standing on end crackling with static, front paws spread wide ready to pounce, tail bristled with electricity, fierce electrified expression.
```

**觉醒形态**：
```
A majestic evolved marten spirit with jet-black and brilliant gold fur with pulsing electric-yellow circuit-like patterns, large blazing electric-white eyes with a golden ring, tiny golden lightning-bolt earrings, a citrine crystal pendant crackling with energy, fur constantly rippling with visible static discharge, flowing ink wash with electrified depth. FULL BODY BATTLE POSE: explosive attack leap with body surrounded by electric arcs, fur blazing with golden lightning, claws extended crackling with thunder energy, devastating electrified fury expression.
```

---

### #8 藤蔓童 (vine_child) — R · 木 · 1-5 波1

**普通形态**：
```
A young vine spirit creature with a small humanoid plant-body made of woven green vines and leaves, round cheerful face with bright green eyes peeping out from a leaf-hood, tiny vine-tendril arms and legs, small flowers budding along the body, a chubby round shape like a walking bush, a tiny jade bead woven into a vine at the neck, warm brown and olive-cream accents with ink wash brush texture. FULL BODY BATTLE POSE: vine-tendrils extended outward in a defensive spread, small thorns visible on the vines, brave determined expression despite small size, ready to entangle.
```

**觉醒形态**：
```
A majestic evolved vine spirit with magnificent blooming vine-body covered in golden flowers and jade-green leaves, large blazing emerald eyes with a golden ring from within a golden leaf-crown, ornate golden vine-patterns, golden flower buds along the tendrils, an ornate jade pendant in golden filigree woven into the body, flowing ink wash with rich botanical depth. FULL BODY BATTLE POSE: vine-tendrils whipping outward with golden thorns, flowers launching pollen projectiles, fierce blooming guardian expression.
```

---

### #9 古榕精 (banyan_elder) — SR · 木 · 1-5 波2

**普通形态**：
```
A young banyan tree spirit with a stout trunk-like body of gnarled brown bark, wise old face with deep amber-green eyes in the bark, spreading root-like legs, branch-like arms with hanging aerial roots, small green leaves forming a canopy-crown on the head, moss and tiny mushrooms growing on the bark, a tiny jade bead on a vine cord, warm brown ink wash with detailed bark texture. FULL BODY BATTLE POSE: roots erupting from below while branches sweep outward, bark plates hardening into armor, commanding ancient forest guardian expression.
```

**觉醒形态**：
```
A majestic evolved banyan tree spirit with magnificent golden-veined bark and sacred emerald leaf-crown, large blazing amber-gold eyes with golden rings, ornate golden root-crown, golden sap-veins throughout the bark, jade crystals growing from the branches, an ornate jade pendant in golden filigree, flowing ink wash with ancient woody depth. FULL BODY BATTLE POSE: roots and branches erupting in all directions with golden nature energy, canopy blazing with life force, supreme ancient forest deity expression.
```

---

### #10 古木神 (ancient_tree_god) — SSR · 木 · 1-5 波3 BOSS

**普通形态**：
```
A massive ancient tree-god spirit with incredible girth and age, wisdom etched in every ring of bark on the warm brown and olive-cream body, large luminous amber-green eyes in the bark with infinite patience, a supreme tree-god form with canopy of a thousand leaves, vast root-system, ecosystem of tiny creatures living within, absolute ancient nature majesty, a tiny jade bead on a thin cord, ink wash brush texture with warm tonal shading. FULL BODY BATTLE POSE: roots erupting everywhere while canopy rains nature-energy, body commanding all plant life, supreme forest god expression.
```

**觉醒形态**：
```
A majestic supreme ancient tree-god with magnificent golden sap-veins and sacred bark-patterns on rich emerald-green and olive-cream body, large blazing emerald-gold eyes with golden rings, ornate golden bark-crown, supreme ancient forest god aura, golden leaves and roots, an ornate jade pendant in golden filigree on a silk cord, flowing ink wash with divine botanical depth. FULL BODY BATTLE POSE: devastating root-and-canopy assault commanding all nature to attack and defend simultaneously, supreme ancient tree deity expression, divine momentum.
```

---

### #11 暮蝠 (dusk_bat) — R · 水 · 2-1 波1

**普通形态**：
```
A young bat spirit with deep purple-black and dark plum membrane wings with shadow-swirl patterns, a small cute bat body with large ears, large round glowing violet eyes with a mysterious curious expression, tiny fangs peeking from the mouth, wing-claws visible at the wing joints, a small fluffy body with dark purple-gray fur, a tiny dark amethyst bead on a thin cord around the neck, ink wash with deep purple tonal shading. FULL BODY BATTLE POSE: wings spread wide in a threatening display with shadow patterns pulsing, swooping down in an aerial dive, fierce nocturnal hunter expression.
```

**觉醒形态**：
```
A majestic evolved bat spirit with magnificent dark amethyst and golden-violet membrane wings with intricate shadow-rune patterns, large blazing violet eyes with a golden ring, ornate golden ear-tip ornaments, golden claw-caps on wing joints, golden shadow-patterns across the body, an ornate amethyst pendant in golden filigree, flowing ink wash with deep mystical depth. FULL BODY BATTLE POSE: devastating shadow-dive with wings creating dark energy trails, body wreathed in purple-gold shadow energy, supreme night predator expression.
```

---

### #12 深渊鳗 (abyss_eel) — SR · 水 · 2-1 波2

**普通形态**：
```
A young eel spirit with sleek dark navy-blue and black body with bioluminescent teal-blue spots along the flanks, a long sinuous serpentine body, large round bright teal eyes with a mysterious deep expression, gaping jaw with tiny sharp teeth, translucent fin running along the spine, a tiny dark sapphire bead on a thin cord, ink wash with deep oceanic tonal shading. FULL BODY BATTLE POSE: body coiled and lunging with jaw open wide, bioluminescent spots pulsing, sinuous predatory strike from the deep.
```

**觉醒形态**：
```
A majestic evolved eel spirit with magnificent obsidian-black and golden-teal body with pulsing golden bioluminescent patterns, large blazing teal eyes with golden rings, ornate golden jaw-plates, golden fin-edges along the spine, golden deep-sea rune markings, an ornate sapphire pendant in golden filigree, flowing ink wash with abyssal depth. FULL BODY BATTLE POSE: devastating abyssal strike with body uncoiling at high speed, golden bioluminescence blazing, supreme deep-sea predator expression.
```

---

### #13 火灵 (fire_wisp) — R · 火 · 2-2 波1

**普通形态**：
```
A young fire elemental wisp spirit with a small round body of living flame in warm orange and bright red, flickering flame-tendrils as limbs, a cute face formed within the fire with large bright yellow-orange eyes with a playful mischievous expression, tiny ember sparks floating around the body, warm golden core visible inside, a tiny ruby bead floating near the center, ink wash with warm flame-tonal shading. FULL BODY BATTLE POSE: flame-body flaring larger and hotter, tendrils reaching outward aggressively, ember sparks intensifying, fierce little fire spirit expression.
```

**觉醒形态**：
```
A majestic evolved fire elemental with magnificent white-hot and golden-vermilion flame body with controlled fire-geometry patterns, large blazing white-gold eyes with a ruby ring, ornate golden flame-crown, golden fire-core blazing with concentrated power, golden ember trails, an ornate ruby pendant floating in golden filigree, flowing ink wash with divine fire depth. FULL BODY BATTLE POSE: erupting with concentrated fire energy in all directions, golden flame-tornado forming, supreme fire elemental expression.
```

---

### #14 炽焰古龙 (inferno_ancient) — SSR · 火 · 2-2 波2 BOSS

**普通形态**：
```
A massive ancient dragon with deep crimson-black and molten-gold body with cracked volcanic scales revealing inner lava, an imposing ancient dragon form, large blazing white-hot eyes with amber cores showing absolute power, grand sweeping horns with molten tips, massive scarred wings, a thick tail with a molten mace-tip, volcanic majesty, ancient scars across the body, a tiny ruby bead on a thin cord, ink wash with volcanic tonal shading. FULL BODY BATTLE POSE: jaws opening to reveal a white-hot inferno within, wings spread creating heat-shimmer, body radiating overwhelming volcanic heat, absolute supreme power expression.
```

**觉醒形态**：
```
A majestic supreme ancient dragon with magnificent obsidian-black and blazing molten-gold body with lava-flow scale patterns, large blazing white-gold eyes with a ruby ring, ornate golden-magma crown between grand horns, magnificent volcanic wings with golden-lava edges, every scale-crack blazing with inner fire, supreme ancient fire god form, an ornate ruby pendant in golden filigree on a silk cord, flowing ink wash with divine volcanic depth. FULL BODY BATTLE POSE: devastating ancient-fire breath unleashing a volcanic inferno, wings creating firestorm updraft, body erupting with primordial fire, absolute supreme dragon god expression.
```

---

### #15 岩龟 (stone_turtle) — R · 土 · 2-3 波1

**普通形态**：
```
A young turtle spirit with olive-green and brown shell with earth-crystal patterns, a round sturdy body with thick legs, large round wise dark amber eyes with a patient calm expression, rocky shell plates with small crystal growths, wrinkled sage-like face, thick scaly legs with stone-textured claws, a tiny amber bead on a thin cord around the neck, ink wash with earthy tonal shading. FULL BODY BATTLE POSE: head and legs retracted partially into shell in defensive stance, shell angled forward like a shield, stalwart immovable guardian expression.
```

**觉醒形态**：
```
A majestic evolved turtle spirit with magnificent dark granite shell with golden amber-crystal veins and formations, large blazing amber eyes with golden rings, ornate golden shell-edge trim, golden crystal growths on the shell, golden earth-rune markings, an ornate amber pendant in golden filigree, flowing ink wash with ancient earthen depth. FULL BODY BATTLE POSE: charging forward with shell as battering ram, golden earth energy radiating from shell cracks, supreme stone guardian expression.
```

---

### #16 岩甲龙 (ironscale_dragon) — SR · 土 · 2-3 波2 BOSS

**普通形态**：
```
A young armored dragon with heavy dark gray and brown iron-like scales in layered armor plating, a powerful stocky dragon body, large fierce amber eyes with a stern military expression, thick curved horns with stone texture, short powerful wings with iron-scale edges, a massive tail with a mace-like club tip, stone-plate underbelly, a tiny amber bead on a thin cord, ink wash with metallic-earth tonal shading. FULL BODY BATTLE POSE: head lowered with horns aimed forward in a charge, tail raised as a weapon, wings flared defensively, indomitable iron dragon expression.
```

**觉醒形态**：
```
A majestic evolved armored dragon with magnificent obsidian and golden-iron scales with glowing amber vein patterns, large blazing topaz eyes with golden rings, ornate golden horn-caps, golden-edged armor plates, golden mace-tail with amber crystals, an ornate amber pendant in golden filigree, flowing ink wash with supreme metallic depth. FULL BODY BATTLE POSE: devastating charge with golden iron-scales flared, tail swinging with golden earth energy, supreme iron dragon warlord expression.
```

---

### #17 雷鹰 (bolt_eagle) — R · 雷 · 2-4 波1

**普通形态**：
```
A young eagle spirit with golden-yellow and dark brown feathers with electric-spark patterns on the wing edges, a young eagle body with broad wings, large sharp electric-yellow eyes with a fierce proud expression, hooked dark beak with a gold tip, powerful talons with tiny sparks between claws, a broad fanned tail with yellow-gold bars, a tiny citrine bead on a thin cord around the neck, ink wash with electrified tonal shading. FULL BODY BATTLE POSE: wings spread wide in a threatening display, talons extended crackling with electricity, head thrown back in a screech, fierce eagle warrior expression.
```

**觉醒形态**：
```
A majestic evolved eagle spirit with brilliant gold and obsidian-brown feathers with pulsing lightning-bolt patterns across the wings, large blazing electric-white eyes with a gold ring, ornate golden head-crest crown, tiny citrine gems embedded in the talons, magnificent crackling storm wings, an ornate citrine pendant in golden filigree, flowing ink wash with thunderous depth. FULL BODY BATTLE POSE: devastating lightning-dive attack with talons leading, body wreathed in electric arcs, wings trailing thunder-bolts, supreme sky predator expression.
```

---

### #18 雷虎 (storm_tiger) — SR · 雷 · 2-4 波2 BOSS

**普通形态**：
```
A young tiger spirit with white and jet-black striped fur with electric-blue lightning patterns running along the stripes, a powerful compact tiger cub body, large fierce electric-yellow eyes with crackling energy, dark striped ears with blue-white inner glow, thick paws with visible spark claws, a thick tail with a lightning-bolt tip shape, a tiny citrine bead on a thin cord around the neck, ink wash with electrified warm tonal shading. FULL BODY BATTLE POSE: lunging forward with claws extended crackling with electricity, body low and coiled, tail lashing with lightning arcs, fierce young thunder beast expression.
```

**觉醒形态**：
```
A majestic evolved tiger spirit with magnificent obsidian-black and brilliant electric-gold body with pulsing storm-patterns, large blazing electric-white eyes with a golden-lightning ring, ornate golden thunder-crown, magnificent electric storm aura, golden lightning-stripes, supreme storm tiger king form, an ornate citrine pendant in golden filigree, flowing ink wash with supreme thunderstorm depth. FULL BODY BATTLE POSE: devastating thunder-roar with body at the center of a lightning-storm, golden electricity radiating in all directions, supreme storm tiger god expression.
```

---

### #19 叶鹿 (leaf_deer) — R · 木 · 2-5 波1

**普通形态**：
```
A young deer spirit with emerald-green and warm fawn-brown body with leaf-vein patterns along the flanks, tiny budding antlers with fresh green sprouts and miniature leaves growing from the tips, large gentle dark-green eyes with a serene peaceful expression, a small jade bead on a vine cord at the neck, white speckled spots on the back like sunlit forest floor, tiny cloven hooves, ink wash brush texture with warm green tonal shading. FULL BODY BATTLE POSE: body poised mid-leap with front legs tucked, antler buds pointing forward, a graceful yet alert stance, determined eyes with natural courage.
```

**觉醒形态**：
```
A majestic evolved deer spirit with magnificent jade-green and golden-fawn body with intricate vine-pattern markings, grand branching antlers with full blooming cherry blossoms and emerald leaves, large blazing emerald-green eyes with a golden-green ring, ornate golden vine circlet on the head, flowing petal-scattered mane, an ornate jade pendant in golden filigree on a silk cord, flowing ink wash with botanical depth. FULL BODY BATTLE POSE: majestic leaping attack with blooming antlers lowered to charge, body stretched mid-gallop, cherry blossom petals trailing behind, fierce forest guardian expression.
```

---

### #20 刺猬 (thorn_hedgehog) — R · 木 · 2-5 波2

**普通形态**：
```
A young hedgehog spirit with dark green and warm brown body, back spines made of living thorny vines with tiny leaves and buds, a round chubby body shape, large round dark-green eyes with a shy timid expression, tiny pink nose, small curled paws, belly fur is soft cream-colored, a few tiny flowers blooming among the thorns, a tiny jade bead on a thin cord around the neck, ink wash with warm green tonal shading. FULL BODY BATTLE POSE: curled into a defensive ball with thorn-vines extended outward bristling, peeking out with fierce determined eyes, ready to roll-charge.
```

**觉醒形态**：
```
A majestic evolved hedgehog spirit with deep emerald-green and golden-brown body with magnificent thorn-vine spines now blooming with vibrant flowers, large blazing emerald eyes with a jade ring, golden thorn-crown circlet, tiny jade bead earrings, vine patterns crawling along the cheeks, an ornate jade pendant in golden filigree on a silk cord, flowing ink wash with rich botanical depth. FULL BODY BATTLE POSE: uncurling from a spin-attack with thorn-vines whipping outward, flowers launching like projectiles, fierce blooming warrior expression.
```

---

### #21 花蛇龙王 (flora_serpent_king) — SR · 木 · 2-5 波3 BOSS

**普通形态**：
```
A magnificent serpent-dragon spirit completely covered in a blooming flower-garden, deep emerald and floral body with warm brown and olive-cream accents, large blazing emerald eyes with a regal nature-king expression, flower-crown horns, vine-scale body, every surface blooming with different flowers, a living serpent-garden of supreme beauty, a tiny jade bead on a thin cord, ink wash with lush botanical tonal shading. FULL BODY BATTLE POSE: body whipping while flowers launch a barrage of nature-projectiles, supreme flora-serpent warrior expression, vines and blossoms erupting.
```

**觉醒形态**：
```
A majestic supreme emerald and golden-floral serpent king with sacred garden patterns on warm brown and olive body, large blazing emerald eyes with golden-jade rings, ornate golden flower-crown, supreme living garden aura, golden vine-scale accents, an ornate jade pendant in golden filigree, flowing ink wash with divine botanical depth. FULL BODY BATTLE POSE: devastating garden-serpent assault with body whipping and flowers exploding with golden nature energy, supreme flora serpent deity expression.
```

---

### #22 朱雀雏 (vermilion_chick) — R · 火 · 3-1 波1

**普通形态**：
```
A young vermilion bird chick with bright scarlet-red and warm gold downy feathers with tiny fire-sparks at the tail tips, a round chubby chick body with small stubby wings, large round bright orange-gold eyes with an eager excited expression, a tiny yellow beak, small red crest feathers on the head, pink feet, a tiny ruby bead on a thin cord around the neck, ink wash with warm flame tonal shading. FULL BODY BATTLE POSE: wings spread wide with tail sparks intensifying, hopping forward in an attack stance, beak open in a tiny fierce chirp.
```

**觉醒形态**：
```
A majestic evolved vermilion bird with magnificent scarlet and gold plumage with flowing flame-pattern tail feathers, large blazing golden-flame eyes with a vermilion ring, ornate tiny golden head-crest, flame patterns along wing edges, elegant longer tail streamers with fire-tips, an ornate ruby pendant in golden filigree on a silk cord, flowing ink wash with divine fire depth. FULL BODY BATTLE POSE: diving attack with wings blazing, tail feathers trailing fire, beak aimed forward like a fiery arrow, fierce young phoenix warrior expression.
```

---

### #23 焰天狮王 (inferno_lion_king) — SR · 火 · 3-1 波2 BOSS

**普通形态**：
```
A magnificent lion spirit with deep crimson and blazing gold mane of heavenly fire, a magnificent lion form wreathed in intense flames, large blazing white-gold eyes with an absolute authority expression, massive burning mane that reaches skyward, golden-fire paws, flame-tail, every hair burning with divine fire, a king-of-all-beasts presence, a tiny ruby bead on a thin cord, ink wash with intense flame tonal shading. FULL BODY BATTLE POSE: massive roar with mane erupting into a pillar of fire, body radiating supreme heat, absolute fire king expression.
```

**觉醒形态**：
```
A majestic supreme lion with magnificent white-gold and supreme vermilion heavenly flame mane blazing with divine fire, large blazing white-gold eyes with a ruby ring, ornate golden emperor-crown with fire-gems, supreme divine-fire aura, golden flame-armor, absolute fire lion god form, an ornate ruby pendant in golden filigree, flowing ink wash with supreme divine fire depth. FULL BODY BATTLE POSE: devastating heavenly fire roar creating a firestorm, mane becoming a fire-tornado, supreme fire lion god expression.
```

---

### #24 寒蛤 (frost_clam) — R · 水 · 3-2 波1

**普通形态**：
```
A young clam spirit with pale blue-white and silver-frost shell plates partially open, a small round creature peeking out from within with large bright icy-blue eyes with a calm cold expression, frost-crystal patterns on the shell exterior, tiny ice-blue tendrils, a pearl visible inside the shell, a tiny sapphire bead on a thin cord, ink wash with cool frost tonal shading. FULL BODY BATTLE POSE: shell snapping partially closed in defensive position while shooting ice-crystal projectiles, frost energy radiating from shell edges, stoic ice guardian expression.
```

**觉醒形态**：
```
A majestic evolved clam spirit with magnificent silver-white and golden-frost shell with intricate ice-crystal and golden vein patterns, large blazing sapphire eyes with golden rings from within, ornate golden shell-edge trim, golden frost-crystal formations, a luminous golden pearl inside, an ornate sapphire pendant in golden filigree, flowing ink wash with glacial depth. FULL BODY BATTLE POSE: shell erupting with golden frost energy, ice-crystals forming a barrier, supreme ice fortress guardian expression.
```

---

### #25 海龙 (ocean_dragon) — SR · 水 · 3-2 波2 BOSS

**普通形态**：
```
A young Chinese ocean dragon with sleek dark navy and turquoise scales, an elegant serpentine body with flowing fins, large fierce deep aquamarine eyes with vertical pupils, ornate whiskers, dark navy mane, fangs visible, graceful water-dragon form, a tiny sapphire bead on a thin cord, ink wash with deep oceanic tonal shading. FULL BODY BATTLE POSE: body coiled and rising from waves with jaw open, fins spread wide creating water-current energy, powerful ocean roar expression.
```

**觉醒形态**：
```
A majestic supreme ocean dragon with magnificent dark sapphire and golden-turquoise scales with ocean-wave patterns, large blazing aquamarine eyes with golden vertical pupils, ornate golden-tipped whiskers, golden horn-caps, dark navy mane with golden thread, golden Daoist divine forehead rune, an ornate sapphire pendant in golden filigree, flowing ink wash with divine oceanic depth. FULL BODY BATTLE POSE: devastating tidal roar with body creating a massive whirlpool, golden ocean energy radiating, supreme ocean dragon deity expression.
```

---

### #26 岩蜥龙 (rock_drake) — R · 土 · 3-3 波1

**普通形态**：
```
A young rock lizard-dragon with dark brown and gray stone-textured scales, a stocky four-legged reptilian body with a broad head, large round amber-brown eyes with a watchful expression, rough rocky ridges along the spine, stone-colored claws, a thick tail with rocky plating, a tiny amber bead on a thin cord, ink wash with earthy stone tonal shading. FULL BODY BATTLE POSE: low stalking pose with body pressed close to ground, tail raised for balance, jaw slightly open showing stone-like teeth, patient predator expression.
```

**觉醒形态**：
```
A majestic evolved rock dragon with magnificent dark obsidian and golden-amber stone scales with glowing vein patterns, large blazing amber eyes with golden rings, ornate golden spine-ridges, golden stone-crown, golden claw-caps, golden earth-rune markings along the body, an ornate amber pendant in golden filigree, flowing ink wash with supreme geological depth. FULL BODY BATTLE POSE: lunging attack with jaw open wide and tail whipping, golden earth energy erupting from the ground, fierce stone dragon warrior expression.
```

---

### #27 磐牛 (boulder_ox) — SR · 土 · 3-3 波2 BOSS

**普通形态**：
```
A young ox spirit with deep chocolate-brown and granite-gray hide with rock-textured patches, a massive stocky body with powerful legs, large horns made of actual boulder-stone with rough rocky texture, large round deep amber eyes with a calm steady expression, broad flat nose with a stone ring, thick hooves that look like carved rock, a tiny amber bead on a thin cord around the neck, ink wash with heavy earthy tonal shading. FULL BODY BATTLE POSE: head lowered with boulder-horns aimed forward in a charge stance, hooves pawing the ground, immovable mountain expression.
```

**觉醒形态**：
```
A majestic evolved ox spirit with dark obsidian-brown and golden-veined rocky hide with glowing amber crack-patterns, massive golden-tipped boulder horns with embedded amber crystals, large blazing topaz eyes with a golden ring, ornate golden nose-ring, stone plates forming natural armor along the shoulders, an ornate amber pendant in golden filigree on a silk cord, flowing ink wash with supreme mountain depth. FULL BODY BATTLE POSE: devastating charging headbutt with boulder-horns glowing, earth cracking underfoot, body surging with mountain-crushing force, unstoppable earthen titan expression.
```

---

### #28 风隼 (wind_falcon) — R · 金 · 3-4 波1

**普通形态**：
```
A young falcon spirit with pale gray-white and silver feathers with wind-swept styling, a sleek streamlined falcon body built for speed, large sharp pale cyan eyes with a focused intense expression, hooked dark beak, pointed wing tips, a banded tail with silver-white bars, small sharp talons, a tiny moonstone bead on a thin cord around the neck, ink wash with cool wind-swept tonal shading. FULL BODY BATTLE POSE: wings tucked in a diving stoop position, body streamlined for maximum speed, intense focused predator expression.
```

**觉醒形态**：
```
A majestic evolved falcon spirit with shimmering silver-white and pearl feathers with swirling wind-trail patterns on the wings, large blazing diamond-white eyes with a cyan ring, ornate tiny silver wind-chime on a leg band, magnificent swept-back crest feathers, wing tips that trail wind energy, an ornate moonstone pendant in golden filigree on a silk cord, flowing ink wash with supreme wind depth. FULL BODY BATTLE POSE: devastating dive-bomb attack at extreme speed, wings creating sonic wind-blade trails, talons extended, unstoppable wind-blade expression.
```

---

### #29 云豹 (cloud_leopard) — R · 金 · 3-4 波2

**普通形态**：
```
A young snow leopard spirit with pure white and pale silver fur with soft cloud-like swirl markings, a sleek graceful feline body, large round bright pale-cyan eyes with a cool aloof expression, long curving tail with wispy cloud-pattern tip, small rounded ears with silver inner coloring, elegant long whiskers, a tiny moonstone bead on a thin cord around the neck, ink wash with cool ethereal tonal shading. FULL BODY BATTLE POSE: crouching low in a stalking pose ready to spring, tail swishing, eyes locked on target with predatory focus, graceful hunter expression.
```

**觉醒形态**：
```
A majestic evolved snow leopard spirit with shimmering pearl-white and silver-lavender fur with flowing cloud and wind-trail patterns, large blazing diamond-white eyes with a pale cyan ring, tiny platinum earrings shaped like clouds, a moonstone pendant on a silk cord, fur that seems to float and billow like clouds, an ornate moonstone pendant in golden filigree, flowing ink wash with ethereal cloud depth. FULL BODY BATTLE POSE: swift pouncing attack from above descending like a cloud, body twisting gracefully mid-air, trail of mist behind, elegant yet lethal predator expression.
```

---

### #30 雷鸣虎 (thunder_roar_tiger) — SR · 金 · 3-4 波3 BOSS

**普通形态**：
```
A powerful large tiger spirit with dark storm-gray and electric-gold striped fur with continuous lightning crackling between the stripes, a powerful large tiger form with storm energy, large blazing electric-gold eyes with a fierce commanding expression, electrified whiskers, thunder-rumble vibrating from the body, storm-clouds forming around the paws, a tiny citrine bead on a thin cord around the neck, ink wash with storm-charged tonal shading. FULL BODY BATTLE POSE: roaring with visible thunderclap shockwave, body discharging lightning in all directions, supreme thunder beast expression.
```

**觉醒形态**：
```
A majestic supreme thunder tiger with magnificent obsidian-black and brilliant electric-gold body with pulsing storm-patterns, large blazing electric-white eyes with a golden-lightning ring, ornate golden thunder-crown, magnificent electric storm aura, golden lightning-stripes, supreme storm tiger king form, an ornate citrine pendant in golden filigree on a silk cord, flowing ink wash with supreme divine thunderstorm depth. FULL BODY BATTLE POSE: devastating thunder-roar attack creating a lightning-storm, body at the center of a thunderstorm, supreme storm tiger god expression.
```

---

### #31 花蛇龙 (flora_lindworm) — R · 木 · 3-5 波1

**普通形态**：
```
A young serpent-dragon with dark emerald-green and brown vine-textured scales, a sinuous serpentine body with small legs, flower buds growing along the spine, large bright amber-green eyes with a cunning expression, small antler-like branches with leaves on the head, moss growing along the coiled body, a tiny jade bead on a thin cord, ink wash with lush green tonal shading. FULL BODY BATTLE POSE: body coiled and striking with jaw open, vine-tendrils extending from the spine, flowers releasing pollen clouds, fierce serpent guardian expression.
```

**觉醒形态**：
```
A majestic evolved flora serpent-dragon with magnificent deep emerald and golden-jade scales with blooming vine-garden patterns, large blazing jade-green eyes with golden rings, ornate golden antler-branches with blooming golden flowers, golden vine-patterns along the body, golden moss creating a miniature garden landscape, an ornate jade pendant in golden filigree, flowing ink wash with supreme botanical depth. FULL BODY BATTLE POSE: devastating strike with flowers and vines erupting in all directions, golden nature energy blazing, fierce flora dragon warrior expression.
```

---

### #32 火龙崽 (fire_dragonling) — R · 火 · 3-5 波2

**普通形态**：
```
A young fire dragon hatchling with bright vermilion-red and orange scales with ember-glow patterns, a small chubby dragon body with stubby wings, large round bright orange eyes with an eager fierce expression, tiny curved horns, a small flame at the tail tip, small sharp claws, oversized head compared to body, a tiny ruby bead on a thin cord, ink wash with warm ember tonal shading. FULL BODY BATTLE POSE: wings spread with small fire-breath attempt, body leaning forward aggressively, tail flame intensifying, fierce baby dragon warrior expression.
```

**觉醒形态**：
```
A majestic evolved fire dragon youth with magnificent crimson-gold and blazing vermilion scales with living fire-pattern markings, large blazing orange-gold eyes with a ruby ring, ornate golden horn-tips, golden wing-edge accents, golden ember-trail from the tail, golden scale-patterns, an ornate ruby pendant in golden filigree, flowing ink wash with intense fire depth. FULL BODY BATTLE POSE: devastating fire-breath attack with wings fully spread, golden flames erupting, body surging with draconic fire power, fierce young fire dragon warrior expression.
```

---

### #33 万象龙神 (cosmos_dragon) — SSR · 全 · 3-5 波3 终极BOSS

**普通形态**：
```
A magnificent five-colored shimmering Chinese dragon spirit with scales cycling through all elemental colors on a pale gold and cream-white body, a supreme Chinese dragon form of divine proportions, large luminous prismatic eyes with infinite depth showing all elements, grand multi-colored flowing mane and whiskers, every scale a different jewel-color, a massive multi-colored pearl at the chin, absolute dragon majesty, golden claws and horns, a tiny sunstone bead on a thin cord, ink wash with prismatic tonal shading. FULL BODY BATTLE POSE: body coiled in a supreme power display, all elemental colors blazing simultaneously, jaw open in a divine roar, absolute supreme dragon god expression.
```

**觉醒形态**：
```
A majestic supreme cosmos dragon-god with magnificent body cycling through all elements with golden divine accents — fire-red, water-blue, earth-brown, wood-green, metal-gold scales flowing in harmony, large blazing prismatic eyes with golden divine rings, ornate golden divine-crown with all-element jewels, golden whiskers, golden divine mane, supreme all-element aura, an ornate prismatic pendant in golden filigree, flowing ink wash with supreme divine cosmic depth. FULL BODY BATTLE POSE: devastating all-element attack with every color blazing in divine harmony, body at the center of an elemental maelstrom, supreme cosmos dragon deity expression, absolute divine power.
```

---

## 五、生成优先级

| 优先级 | 内容 | 数量 |
|--------|------|------|
| **P0** | BOSS（觉醒形态）：古木神、炽焰古龙、花蛇龙王、焰天狮王、海龙、磐牛、雷鸣虎、万象龙神 | 8 张 |
| **P1** | 其余 BOSS（觉醒形态）：岩甲龙、雷虎 | 2 张 |
| **P2** | 所有 33 只的普通形态 | 33 张 |
| **P3** | 非 BOSS 的觉醒形态（备用） | 23 张 |
| **合计** | | **66 张** |

> 每张图为 2:1 横版，剪裁后得到 2 张正方形图（头像 + 全身），总共可得 **132 张** 最终素材。

---

## 六、文件命名规范

| 类型 | 生成图文件名 | 剪裁后文件 |
|------|------------|-----------|
| 普通形态 | `{pet_id}_normal_combined.png` | `{pet_id}.png`（全身）+ `{pet_id}_avatar.png`（头像） |
| 觉醒形态 | `{pet_id}_awakened_combined.png` | `{pet_id}_awakened.png`（全身）+ `{pet_id}_awakened_avatar.png`（头像） |

战斗中使用的路径：
- 普通敌人全身：`assets/enemies/stage/{pet_id}.png`
- BOSS 觉醒全身：`assets/enemies/stage/{pet_id}_awakened.png`
- 头像（宠物池扩展）：`assets/pets/{pet_id}_avatar.png`
