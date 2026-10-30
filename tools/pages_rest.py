"""How we work, about, contact, demos hub, insights, legal, 404."""
from lib import *
from pages_main import demos_data, services_data


# ------------------------------------------------------------------ how we work

def how_we_work(lang):
    t = mk(lang)
    body = page_hero(lang, [(t('How we work', '合作方式'), None)], t('How we work', '合作方式'),
                     t('A short, staged process. You see the scope and price before work starts, and you can stop after any stage.',
                       '一个简短、分阶段的流程。开工前你会先看到范围和价格，并且可以在任何阶段停下来。'))
    phases = [
        (t('01 · Assess', '01 · 评估'),
         t('We map one process end to end: the steps, volumes, error cases and who touches what. We sample real inputs and measure how long the work takes today.',
           '我们把一个流程从头到尾梳理清楚：步骤、量级、出错情形，以及谁在经手。抽取真实样本，并测量现在所需的时间。'),
         [t('Findings document with a baseline of the current process', '含现状基线的评估文档'),
          t('Recommendation: automate, change the process first, or leave as is', '建议：自动化、先优化流程，或维持现状'),
          t('Written scope and price for the next stage', '下一阶段的书面范围与报价')]),
        (t('02 · Prototype', '02 · 原型'),
         t('We build a working version on your real samples, and compare its output with what your team produces today.',
           '用你的真实样本做出可运行的版本，并把它的结果与团队现在的产出做对比。'),
         [t('Working prototype and a results comparison', '可运行的原型与结果对比'),
          t('List of exception cases found', '发现的异常情形清单'),
          t('Go / no-go recommendation', '继续或终止的建议')]),
        (t('03 · Deploy', '03 · 上线'),
         t('We connect the workflow to your systems with human review switched on, logging enabled and a clear way to pause it.',
           '把流程对接到你的系统，开启人工复核和日志，并保留明确的暂停方式。'),
         [t('Production workflow with review queue and audit log', '带复核队列和审计日志的正式流程'),
          t('Runbook: monitor, pause, roll back', '运行手册：监控、暂停、回退'),
          t('Hand-over session for your team', '面向你团队的交接会')]),
        (t('04 · Improve', '04 · 改进'),
         t('Each month we review exceptions and errors with you, tighten rules and report against the baseline.',
           '每月与你一起复盘异常和错误，收紧规则，并对照基线汇报。'),
         [t('Monthly review of exceptions and results', '每月的异常与结果复盘'),
          t('Updated rules and documentation', '更新后的规则与文档'),
          t('Report against the original baseline', '对照原始基线的报告')])]
    inner = "".join('<div class="card" style="margin-bottom:24px"><h3>%s</h3><p>%s</p><ul>%s</ul></div>' % (
        a, b, "".join("<li>%s</li>" % x for x in c)) for a, b, c in phases)
    body += section(inner, t('Process', '流程'), t('Four stages', '四个阶段'), '', '', narrow=True)
    body += section(cards([
        ('', t('Communication', '沟通'), t('One named contact, a shared written log of decisions, and regular check-ins by video call.', '一位固定联系人、共享的书面决策记录，以及定期视频沟通。'), None, None, None),
        ('', t('Data handling', '数据处理'), t('Minimum access, your own accounts where possible, and handling terms agreed in writing first. See our security practices.', '最小权限，尽量使用你自己的账号，并事先书面约定处理条款。详见我们的安全实践。'), None, None, None),
        ('', t('Documentation', '文档'), t('Everything we build is documented in plain language so your team can run it without us.', '我们交付的一切都有平实的文档，让你的团队不依赖我们也能运行。'), None, None, None)], 3),
        t('Working agreement', '合作约定'), t('What to expect', '你可以期待什么'), '', 'tint')
    body += section(cards([
        ('', t('Assessment', '评估'), t('Fixed scope and price. A good first step.', '范围和价格固定，是不错的第一步。'), None, None, None),
        ('', t('Build project', '搭建项目'), t('Quoted per project after the assessment.', '评估之后按项目报价。'), None, None, None),
        ('', t('Monthly support', '月度支持'), t('Monthly retainer for monitoring and improvement.', '按月订阅，用于监控与改进。'), None, None, None)], 3),
        t('Pricing', '收费'), t('Quoted up front, never open-ended', '事先报价，不做无限期投入'),
        t('We do not publish rate cards because scope varies. Every engagement is quoted in writing before work begins.', '范围因项目而异，所以不公布价目表。所有合作开工前都会书面报价。'))
    body += cta(lang)
    return (t('How We Work | DXC Group Inc', '合作方式 | DXC Group Inc'),
            t('Our four-stage process: assess, prototype, deploy and improve. Fixed-scope start, written quotes, human review and documentation built in.',
              '我们的四阶段流程：评估、原型、上线、改进。固定范围起步、书面报价、内置人工复核与文档。'),
            body, graph(org_schema()))


# ------------------------------------------------------------------ about

def about(lang):
    t = mk(lang)
    body = page_hero(lang, [(t('About', '关于我们'), None)], t('A small, independent firm', '一家小而独立的公司'),
                     t('DXC Group Inc. is a California corporation founded in 2016. We help operations teams and online sellers remove repetitive work with AI-assisted workflows.',
                       'DXC Group Inc. 是一家 2016 年成立的加州公司，我们用 AI 辅助的工作流帮助运营团队和线上卖家去掉重复性工作。'))
    left = f"""<h2>{t('Who we are', '我们是谁')}</h2>
<p>{t('We are a small consultancy that works directly with each client. You talk to the people doing the work, not an account layer.', '我们是一家直接与每位客户合作的小型咨询公司。你沟通的对象就是实际做事的人，而不是中间的客户经理层。')}</p>
<p>{t('We deliver remotely, which keeps overhead low and lets us work with teams anywhere in the United States.', '我们通过远程方式交付，这样成本更低，也能与美国各地的团队合作。')}</p>
<h2>{t('What we do not do', '我们不做什么')}</h2>
{bullets([t('We do not promise headcount reductions or specific savings before measuring your process.', '在测量你的流程之前，不承诺减员或具体的节省金额。'),
          t('We do not automate irreversible actions without a review step.', '没有复核环节，不对不可撤销的操作做自动化。'),
          t('We do not resell client data or use it for anything outside the engagement.', '不转售客户数据，也不将其用于项目之外的任何用途。'),
          t('We do not take vendor commissions, so our recommendations stay independent.', '不收取供应商佣金，因此我们的建议保持独立。')])}
<h2>{t('Certifications', '认证情况')}</h2>
<p>{t('We do not currently hold SOC 2 or similar attestations. Our security practices are described plainly on the security page, and we agree data handling terms with each client in writing.', '我们目前没有 SOC 2 等认证。我们的安全实践在安全页中如实说明，并与每位客户书面约定数据处理条款。')}</p>"""
    right = facts([(t('Legal name', '公司名称'), 'DXC Group Inc.'),
                   (t('Entity type', '主体类型'), t('California corporation', '加州公司')),
                   (t('Established', '成立时间'), t('2016', '2016 年')),
                   (t('Delivery', '交付方式'), t('Remote', '远程')),
                   (t('Focus', '业务重点'), t('Workflow automation & AI advisory', '流程自动化与 AI 咨询')),
                   (t('Contact', '联系邮箱'), '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL))])
    body += section('<div class="split"><div class="prose">%s</div><aside class="aside">%s</aside></div>' % (left, right))
    body += section(cards([
        ('01', t('Plain language', '平实表达'), t('Reports, rules and documentation are written so a non-specialist can follow them.', '报告、规则和文档的写法让非专业人士也能看懂。'), None, None, None),
        ('02', t('Evidence over claims', '以事实说话'), t('We show working demos and baselines instead of general promises.', '我们展示可运行的演示和基线数据，而不是笼统的承诺。'), None, None, None),
        ('03', t('Right-sized tools', '合适的工具'), t('If a simple rule does the job, we use the rule. Models are used where they add value.', '简单规则能解决的就用规则，模型只用在真正有价值的地方。'), None, None, None)], 3),
        t('Values', '价值观'), t('How we work with clients', '我们如何与客户合作'), '', 'tint')
    body += cta(lang)
    return (t('About | DXC Group Inc', '关于我们 | DXC Group Inc'),
            t('DXC Group Inc. is a small, independent California corporation (est. 2016) offering remote AI consulting and workflow automation.',
              'DXC Group Inc. 是一家小而独立的加州公司（2016 年成立），提供远程 AI 咨询与流程自动化服务。'),
            body, graph(org_schema()))


# ------------------------------------------------------------------ contact

def contact(lang):
    t = mk(lang)
    body = page_hero(lang, [(t('Contact', '联系'), None)], t('Talk to us', '联系我们'),
                     t('Tell us about the process that eats your week. A few lines are enough.', '告诉我们哪个流程最耗时间，简单几句话就够。'))
    form = f"""<form action="mailto:{EMAIL}" method="post" enctype="text/plain">
<label>{t('Name', '姓名')}<input name="name" required autocomplete="name"></label>
<label>{t('Work email', '工作邮箱')}<input type="email" name="email" required autocomplete="email"></label>
<label>{t('Company', '公司')}<input name="company" autocomplete="organization"></label>
<label>{t('Area of interest', '感兴趣的方向')}
<select name="interest"><option>{t('Business workflow automation', '企业流程自动化')}</option><option>{t('E-commerce operations', '电商运营')}</option><option>{t('AI adoption advisory', 'AI 落地咨询')}</option><option>{t('Not sure yet', '暂不确定')}</option></select></label>
<label>{t('What would you like to improve?', '你希望改进什么？')}<textarea name="message" required></textarea></label>
<button class="btn" type="submit">{t('Send message', '发送消息')}</button>
<p class="small">{t('This opens your email app. Please do not include confidential data in the first message.', '点击后会打开你的邮件应用。首次沟通请不要包含机密数据。')}</p>
</form>"""
    side = f"""<h3>{t('Email', '邮箱')}</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h3>{t('What happens next', '接下来会发生什么')}</h3>
{steps([(t('We read it', '我们阅读'), t('We reply within two business days.', '两个工作日内回复。')),
        (t('A short call', '简短通话'), t('Twenty to thirty minutes by video to understand the process.', '二三十分钟视频沟通，了解流程。')),
        (t('A written proposal', '书面方案'), t('A fixed-scope assessment, or an honest “not worth automating”.', '固定范围的评估方案，或者坦率地告诉你“不值得自动化”。'))]).replace('class="steps"', 'class="steps" style="grid-template-columns:1fr"')}
<h3 style="margin-top:28px">{t('Helpful to include', '建议附上')}</h3>
{bullets([t('What the process is and who does it today', '流程是什么、目前由谁来做'),
          t('Roughly how often it happens', '大致发生的频率'),
          t('Which systems are involved', '涉及哪些系统')])}"""
    body += section('<div class="contact"><div class="prose">%s</div>%s</div>' % (side, form))
    return (t('Contact | DXC Group Inc', '联系我们 | DXC Group Inc'),
            t('Contact DXC Group Inc. about workflow automation, e-commerce operations or AI advisory. Email sales@dxcgroupinc.com.',
              '就流程自动化、电商运营或 AI 落地咨询联系 DXC Group Inc。邮箱 sales@dxcgroupinc.com。'),
            body, graph(org_schema()))


# ------------------------------------------------------------------ demos hub

def demos_hub(lang):
    t = mk(lang)
    body = page_hero(lang, [(t('Demos', '演示应用'), None)], t('Working demos', '可运行的演示'),
                     t('Three small applications you can try with sample data. They show the shape of our work.', '三个可以用示例数据试用的小应用，展示我们工作的形态。'))
    body += section(cards([(d['num'], d['title'], d['text'], None, url('en', 'demos/' + d['slug']), t('Try the demo →', '试用演示 →')) for d in demos_data(lang)]) +
                    '<p class="notice" style="margin-top:32px">%s</p>' % t(
                        'Demos run entirely in your browser and upload nothing. They use sample data and simple rules, not client data. Production versions read real documents, connect to your systems, use a language model where it helps, and keep a review queue and audit log. The demo interface is in English.',
                        '演示完全在你的浏览器中运行，不会上传任何内容。使用的是示例数据和简单规则，并非客户数据。正式版本会读取真实文档、对接你的系统、在有价值之处使用语言模型，并带有复核队列和审计日志。演示界面为英文。'))
    body += cta(lang)
    return (t('Demos | DXC Group Inc', '演示应用 | DXC Group Inc'),
            t('Try working demos of invoice matching, support ticket triage and contract information extraction. Runs in your browser with sample data.',
              '试用发票对账、客服工单分流和合同信息抽取的可运行演示，在浏览器中用示例数据运行。'),
            body, graph(org_schema()))


# ------------------------------------------------------------------ insights

def articles():
    return [
        dict(slug="which-processes-to-automate", date="2026-10-30", services=["workflow-automation", "ai-advisory"],
             en=dict(title="Which processes are worth automating? A five-question screen",
                     desc="A simple screen for deciding whether a process is a good candidate for AI-assisted automation.",
                     body=[("p", "Not every slow process should be automated. Some are slow because the underlying decision is hard, or because the process itself is broken. Five questions help separate good candidates from poor ones."),
                           ("h", "1. How often does it happen?"), ("p", "Volume pays for the work of building and maintaining automation. A task done twice a month rarely justifies it. A task done every hour usually does."),
                           ("h", "2. Can you write down what “correct” looks like?"), ("p", "If two experienced people would disagree about the right answer, a rule or a model will not settle it. Start with work where correctness is clear: an amount matches or it does not, a field is present or it is not."),
                           ("h", "3. How varied are the inputs?"), ("p", "Fixed-format inputs can be handled with plain rules. Varied inputs, such as invoices from many suppliers or free-text emails, are where language models add real value."),
                           ("h", "4. What does a mistake cost?"), ("p", "A wrong category on a support ticket is cheap to fix. A wrong payment is not. The higher the cost, the more review you need, and the less it makes sense to remove the person entirely."),
                           ("h", "5. Can a reviewer catch errors?"), ("p", "Good candidates let a person scan exceptions quickly. If checking the result takes as long as doing the work, automation will not save time."),
                           ("h", "What to do with the answers"), ("p", "Processes that score well on all five are good pilots. Processes that fail the second question usually need clearer rules before any technology. Measure the current process first, so you can tell whether the change actually helped.")]),
             zh=dict(title="哪些流程值得自动化？五个问题的筛选法",
                     desc="一个简单的筛选方法，用来判断某个流程是否适合 AI 辅助自动化。",
                     body=[("p", "不是每个慢的流程都该自动化。有些流程慢，是因为决策本身很难，或者流程本身就有问题。用下面五个问题，可以把合适的候选和不合适的区分开。"),
                           ("h", "1. 发生得有多频繁？"), ("p", "搭建和维护自动化需要投入，量大才划算。每月做两次的事很少值得，每小时都在做的事通常值得。"),
                           ("h", "2. 能写下“正确”是什么样吗？"), ("p", "如果两位有经验的人对正确答案有分歧，规则或模型也解决不了。先从正确与否很清楚的工作入手：金额对得上或对不上，字段有或没有。"),
                           ("h", "3. 输入的差异有多大？"), ("p", "格式固定的输入用普通规则就能处理。差异大的输入，比如来自众多供应商的发票或自由文本邮件，才是语言模型真正有价值的地方。"),
                           ("h", "4. 出错的代价是什么？"), ("p", "客服工单分错类很容易纠正，付款付错就不一样。代价越高，越需要复核，也越不应该把人完全拿掉。"),
                           ("h", "5. 复核的人能发现错误吗？"), ("p", "好的候选能让人快速扫一眼异常。如果检查结果和亲自做一样费时间，自动化就省不了时间。"),
                           ("h", "如何使用这些答案"), ("p", "五项都得分高的流程适合做试点。第二个问题不过关的流程，通常需要先把规则理清楚，再谈技术。先测量现状，才能判断改动是否真的有效。")])),
        dict(slug="human-in-the-loop", date="2026-10-30", services=["workflow-automation", "ai-advisory"],
             en=dict(title="Designing human review into AI workflows",
                     desc="How to place people in an AI-assisted workflow so errors are caught early and trust builds over time.",
                     body=[("p", "An AI-assisted workflow without a review step is a risk. One with a badly placed review step is a bottleneck. The goal is to put people where their judgement matters and keep them away from routine work."),
                           ("h", "Route by confidence and by consequence"), ("p", "Send an item to a person when the system is unsure, or when the action is costly or hard to undo, even if the system is sure. Everything else can go through."),
                           ("h", "Show the reason"), ("p", "A reviewer who sees only “flagged” has to redo the work. A reviewer who sees “amount differs from the purchase order by 4%” can decide in seconds."),
                           ("h", "Keep an exception queue, not a free-for-all"), ("p", "One queue with owners and a time target keeps exceptions from piling up. Track what lands there, because that list tells you which rules to improve next."),
                           ("h", "Log every decision"), ("p", "Record what the system did, what the reviewer decided and when. This supports audits, debugging and the conversation about whether to loosen or tighten review."),
                           ("h", "Plan the off switch"), ("p", "Decide in advance how to pause the workflow and how to revert its changes. A workflow you can stop is a workflow people are willing to start."),
                           ("h", "Loosen review gradually"), ("p", "Start with review on everything, then relax it for categories where results have been consistently correct. Let evidence, not enthusiasm, drive that decision.")]),
             zh=dict(title="如何把人工复核设计进 AI 工作流",
                     desc="如何在 AI 辅助的工作流里安排人，让错误尽早被发现，并让信任逐步建立。",
                     body=[("p", "没有复核环节的 AI 工作流是风险，复核位置不当的则是瓶颈。目标是把人放在判断真正重要的地方，让他们远离例行工作。"),
                           ("h", "按把握程度和后果来分流"), ("p", "系统没把握时，或者操作代价高、难以撤销时（即使系统很有把握），交给人处理。其余的可以直接通过。"),
                           ("h", "把原因展示出来"), ("p", "只看到“已标记”的复核人员只能重做一遍。看到“金额与采购订单相差 4%”的复核人员几秒钟就能判断。"),
                           ("h", "设一个有负责人的异常队列"), ("p", "一个有负责人和时间目标的队列，能避免异常堆积。记录进入队列的内容，这份清单会告诉你下一步该改进哪些规则。"),
                           ("h", "记录每个决定"), ("p", "记下系统做了什么、复核人决定了什么、发生在何时。这有助于审计、排错，也有助于讨论复核该放松还是收紧。"),
                           ("h", "提前规划关闭开关"), ("p", "事先确定如何暂停工作流、如何回退它的改动。可以随时停下的流程，人们才愿意启动。"),
                           ("h", "逐步放宽复核"), ("p", "一开始对所有内容都复核，之后对结果一贯正确的类别逐步放宽。让证据而不是热情来驱动这个决定。")])),
        dict(slug="ecommerce-support-cost", date="2026-10-30", services=["ecommerce-operations"],
             en=dict(title="Reducing e-commerce support cost without hurting quality",
                     desc="Practical steps for cutting repetitive support work in an online store while keeping answers accurate.",
                     body=[("p", "Support cost in an online store grows with order volume, but much of the work is repetitive. The aim is to free agents from the repeats so they can handle the cases that need care."),
                           ("h", "Start by measuring"), ("p", "Export a few weeks of tickets and group them by reason. Most stores find a small number of reasons, such as order status, returns and address changes, make up most of the volume. That is where to begin."),
                           ("h", "Triage before you answer"), ("p", "Sorting by intent and urgency means billing errors and damaged goods reach an agent first, while simple status questions can follow a standard path."),
                           ("h", "Draft, do not auto-send"), ("p", "Generating a draft from your policies and help articles saves typing time, and the agent still checks facts such as order details before sending."),
                           ("h", "Fix the source of repeat questions"), ("p", "If many customers ask where their order is, the confirmation email or tracking page may be unclear. Removing the cause beats answering faster."),
                           ("h", "Write the returns playbook"), ("p", "Clear rules for when to refund, replace or escalate remove guesswork, shorten handling time and make quality more even across agents."),
                           ("h", "Track the right measures"), ("p", "Watch time to first reply, how often a customer needs a second contact and customer satisfaction, not just cost per ticket. Cost cuts that hurt those measures are not savings.")]),
             zh=dict(title="在不影响服务质量的前提下降低电商客服成本",
                     desc="在保证回答准确的前提下，减少网店客服重复性工作的实用步骤。",
                     body=[("p", "网店的客服成本随订单量增长，但其中很多工作是重复的。目标是让客服从重复问题中解放出来，把精力用在需要细心处理的案例上。"),
                           ("h", "先测量"), ("p", "导出几周的工单，按原因分组。大多数店铺会发现，订单状态、退货、改地址等少数几类原因占了大部分量，从这里入手。"),
                           ("h", "先分流，再回答"), ("p", "按意图和紧急程度分类，让账单错误和商品损坏优先到达客服手中，简单的状态查询则走标准流程。"),
                           ("h", "生成草稿，不要自动发送"), ("p", "依据你的政策和帮助文档生成草稿，能节省打字时间；发送前客服仍会核对订单详情等事实。"),
                           ("h", "从源头减少重复问题"), ("p", "如果很多客户都在问订单到哪了，可能是确认邮件或物流页面不够清楚。消除原因比回答得更快更有效。"),
                           ("h", "写好退换货规范"), ("p", "明确什么情况退款、换货或升级，可以减少猜测、缩短处理时间，也让不同客服之间的质量更均衡。"),
                           ("h", "关注正确的指标"), ("p", "除了单张工单成本，也要看首次回复时间、客户需要二次联系的比例和满意度。损害这些指标的成本削减并不是真正的节省。")])),
    ]


def insights_hub(lang):
    t = mk(lang)
    arts = articles()
    body = page_hero(lang, [(t('Insights', '洞察'), None)], t('Insights', '洞察'),
                     t('Practical notes on automating real work with AI, written from the work itself.', '关于用 AI 自动化真实工作的实用笔记。'))
    items = [('', a[lang]['title'], a[lang]['desc'], None, url(lang, 'insights/' + a['slug']), t('Read →', '阅读 →')) for a in arts]
    body += section(cards(items, 3))
    body += cta(lang)
    return (t('Insights | DXC Group Inc', '洞察 | DXC Group Inc'),
            t('Practical articles on workflow automation, human review and e-commerce support from DXC Group Inc.', 'DXC Group Inc 关于流程自动化、人工复核和电商客服的实用文章。'),
            body, graph(org_schema()))


def article_page(lang, a):
    t = mk(lang)
    c = a[lang]
    prose = ""
    for kind, text in c['body']:
        prose += ("<h2>%s</h2>" if kind == "h" else "<p>%s</p>") % text
    hero = page_hero(lang, [(t('Insights', '洞察'), url(lang, 'insights')), (c['title'], None)], c['title'], c['desc'],
                     '<p class="article-meta">DXC Group Inc. · %s</p>' % a['date'])
    rel = ""
    svs = [s for s in services_data(lang) if s['slug'] in a['services']]
    rel = '<div class="rel"><h3>%s</h3><ul>%s</ul></div>' % (
        t('Related services', '相关服务'),
        "".join('<li><a href="%s">%s</a></li>' % (url(lang, 'services/' + s['slug']), s['title']) for s in svs))
    body = hero + section('<div class="prose">%s%s</div>' % (prose, rel), narrow=True) + cta(lang)
    schema = graph(org_schema(), {
        "@type": "Article", "headline": c['title'], "description": c['desc'], "datePublished": a['date'],
        "inLanguage": "en" if lang == "en" else "zh-Hans",
        "author": {"@id": BASE + "/#org"}, "publisher": {"@id": BASE + "/#org"},
        "mainEntityOfPage": BASE + url(lang, 'insights/' + a['slug'])})
    return c['title'], c['desc'], body, schema


# ------------------------------------------------------------------ legal (English only)

def legal(kind):
    lang = "en"
    texts = {
        "privacy": ("Privacy Policy", "How DXC Group Inc collects, uses and protects personal information.", """
<p>DXC Group Inc. (“DXC Group”, “we”) is a California corporation. This policy explains what information we collect through dxcgroupinc.com and in the course of client engagements.</p>
<h2>Information we collect</h2>
<ul><li><strong>Contact messages.</strong> When you email us or use the contact form, we receive your name, email address and the content of your message.</li>
<li><strong>Basic site data.</strong> Our hosting provider may log technical data such as IP address, browser type and pages requested, for security and reliability.</li>
<li><strong>Fonts.</strong> This site loads fonts from Google Fonts, which receives your IP address when the page loads.</li>
<li><strong>Demo tools.</strong> The demos run in your browser. Text you enter is not sent to our servers.</li></ul>
<p>We do not use advertising cookies or third-party analytics on this site.</p>
<h2>How we use it</h2>
<p>We use contact information to respond to enquiries and to manage client relationships. We do not sell personal information.</p>
<h2>Client data</h2>
<p>Data we receive while delivering services is handled under the written agreement for that engagement, which sets out scope, access, retention and deletion.</p>
<h2>Your choices</h2>
<p>You may ask us to access, correct or delete personal information we hold about you. California residents may have additional rights under applicable law.</p>
<h2>Contact</h2>
<p>Email <a href="mailto:%s">%s</a>.</p>""" % (EMAIL, EMAIL)),
        "terms": ("Terms of Use", "Terms governing use of the DXC Group Inc website.", """
<p>These terms apply to your use of dxcgroupinc.com. Services we provide to clients are governed by a separate written agreement.</p>
<h2>Use of the site</h2>
<p>You may browse the site and try the demo tools for lawful, personal or internal business evaluation purposes. Do not attempt to disrupt the site or access it in unauthorized ways.</p>
<h2>Demonstrations</h2>
<p>Demos and examples are illustrations built with sample data. They are not descriptions of client work and are provided without warranty of accuracy or fitness for a particular purpose. Do not enter confidential or personal data into them.</p>
<h2>Articles</h2>
<p>Articles are general information, not legal, financial or compliance advice.</p>
<h2>Intellectual property</h2>
<p>Site content and demo code are owned by DXC Group Inc. unless stated otherwise. Do not copy or redistribute them without permission.</p>
<h2>Disclaimer and liability</h2>
<p>The site is provided “as is”. To the extent permitted by law, DXC Group Inc. is not liable for damages arising from your use of the site.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of California.</p>
<h2>Contact</h2>
<p>Email <a href="mailto:%s">%s</a>.</p>""" % (EMAIL, EMAIL)),
        "security": ("Security Practices", "How DXC Group Inc approaches data security in client engagements.", """
<p>This page describes how we approach security when working with client data. It is a statement of practice, not a certification. We do not currently hold SOC 2 or similar attestations.</p>
<h2>Principles</h2>
<ul><li><strong>Minimum access.</strong> We request only the data and permissions an engagement needs.</li>
<li><strong>Your environment first.</strong> Where possible, work runs in accounts and systems you own and control.</li>
<li><strong>Written terms.</strong> Data handling, retention and deletion are agreed in writing before work starts.</li>
<li><strong>Human review.</strong> Automated workflows we build route exceptions and sensitive actions to a person, and keep logs.</li>
<li><strong>Sample data.</strong> Where possible we develop against samples with sensitive details removed.</li></ul>
<h2>Third-party AI services</h2>
<p>If a solution uses an external AI provider, we tell you which one, what data is sent and under which provider terms, and we use options that fit your requirements.</p>
<h2>This website</h2>
<p>The site is static and served through Cloudflare. It has no user accounts and stores no form data; the contact form opens your email application.</p>
<h2>Reporting a concern</h2>
<p>To report a security issue, email <a href="mailto:%s">%s</a>.</p>""" % (EMAIL, EMAIL)),
    }
    title, desc, inner = texts[kind]
    body = page_hero(lang, [(title, None)], title, desc, '<p class="article-meta">Last updated: %s</p>' % UPDATED)
    body += section('<div class="prose">%s</div>' % inner, narrow=True)
    return title + " | DXC Group Inc", desc, body, None


def not_found():
    body = page_hero("en", [("404", None)], "Page not found", "The page you were looking for does not exist or has moved.",
                     '<div class="actions"><a class="btn" href="/">Go to the home page</a></div>')
    return "Page not found | DXC Group Inc", "Page not found.", body, None
