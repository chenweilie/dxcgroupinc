"""Home, services, how-we-work, about, contact."""
from lib import *

# ------------------------------------------------------------------ shared data

def faq_items(lang):
    t = mk(lang)
    return [
        (t("Do you work with clients remotely?", "你们可以远程合作吗？"),
         t("Yes. All engagements are delivered remotely through video calls, shared documents and the tools your team already uses, such as your ticketing system, spreadsheets or ERP.",
           "可以。所有项目都通过视频会议、共享文档和你团队已有的工具（如工单系统、表格或 ERP）远程交付。")),
        (t("Which processes are a good fit for AI automation?", "哪些流程适合 AI 自动化？"),
         t("High-volume, rules-heavy work with semi-structured inputs such as invoices, orders, support tickets and contracts, where a person can review the exceptions. Rare one-off tasks and decisions without written criteria are usually not worth automating.",
           "量大、规则多、输入半结构化的工作，例如发票、订单、客服工单和合同，并且可以由人复核异常。罕见的一次性任务，以及没有书面标准的决策，通常不值得自动化。")),
        (t("How do you handle sensitive data?", "如何处理敏感数据？"),
         t("We ask for the minimum access an engagement needs, prefer to work inside accounts and systems you control, and agree data handling, retention and deletion in writing before work starts.",
           "只申请项目所需的最小权限，优先在你自己掌控的账号和系统中工作，并在开工前书面约定数据处理、保留与删除方式。")),
        (t("How does pricing work?", "如何收费？"),
         t("We start with a fixed-scope assessment. Build and support work is then quoted per project or as a monthly retainer. You see the scope and price before anything starts.",
           "先做固定范围的评估；之后的搭建与支持按项目报价，或按月订阅。任何工作开始前你都会先看到范围和价格。")),
        (t("Which AI models do you use?", "你们使用哪些 AI 模型？"),
         t("We choose by task, cost and your data requirements, and we tell you which provider is involved and what data would be sent to it. Where rules are enough, we use rules instead of a model.",
           "按任务、成本和你的数据要求来选择，并告诉你涉及哪家服务商、会发送哪些数据。规则就能解决的地方，我们用规则而不是模型。")),
        (t("Will this replace our staff?", "这会取代我们的员工吗？"),
         t("The goal is to remove repetitive steps so people spend their time on exceptions and judgement. Staffing decisions are yours, and we do not promise headcount changes.",
           "目标是去掉重复性环节，让人把时间用在异常和判断上。人员安排由你决定，我们不承诺任何编制变化。")),
    ]


def services_data(lang):
    t = mk(lang)
    return [
        dict(slug="workflow-automation",
             num="01",
             title=t("Business workflow automation", "企业流程自动化"),
             short=t("Turn multi-system, copy-and-paste processes into reliable pipelines.", "把跨系统、靠复制粘贴的流程变成可靠的自动化流水线。"),
             bullets=[t("Invoice, order and reconciliation flows", "发票、订单与对账流程"),
                      t("Document and email triage", "文档与邮件分拣"),
                      t("Hand-offs to your ERP, CRM or spreadsheets", "对接 ERP、CRM 或表格")]),
        dict(slug="ecommerce-operations",
             num="02",
             title=t("E-commerce operations", "电商运营"),
             short=t("Standardize the repetitive, costly parts of running an online store.", "把线上店铺中重复且耗成本的环节标准化。"),
             bullets=[t("Listing and product-data cleanup", "商品信息与刊登数据整理"),
                      t("Support ticket sorting and drafted replies", "客服工单分流与回复草稿"),
                      t("Return and exception handling playbooks", "退换货与异常处理规范")]),
        dict(slug="ai-advisory",
             num="03",
             title=t("AI adoption advisory", "AI 落地咨询"),
             short=t("A clear, practical view of where AI helps your team and where it does not.", "清楚、务实地判断 AI 在哪些环节能帮到团队，哪些不能。"),
             bullets=[t("Use-case ranking and pilot roadmap", "场景优先级与试点路线图"),
                      t("Build-vs-buy and vendor review", "自建与采购、供应商评估"),
                      t("Risk, review and rollout guidelines", "风险、复核与推广准则")]),
    ]


def demos_data(lang):
    t = mk(lang)
    return [
        dict(slug="invoice-matching", num="DEMO 01",
             title=t("Invoice and order reconciliation", "发票与订单对账"),
             text=t("Match supplier invoices to purchase orders and surface only the exceptions.", "把供应商发票与采购订单匹配，只呈现异常项。")),
        dict(slug="ticket-triage", num="DEMO 02",
             title=t("E-commerce support triage", "电商客服工单分流"),
             text=t("Sort support tickets by category and priority and draft a first reply for an agent.", "按类别和优先级分流客服工单，并为客服生成回复草稿。")),
        dict(slug="document-extraction", num="DEMO 03",
             title=t("Contract information extraction", "合同信息抽取"),
             text=t("Turn contract text into structured fields and flag what is missing.", "把合同文本整理成结构化字段，并标出缺失项。")),
    ]


# ------------------------------------------------------------------ home

def home(lang, insights):
    t = mk(lang)
    hero = f"""<section class="hero"><div class="wrap">
<div>
<p class="eyebrow">{t('AI consulting &amp; automation', 'AI 咨询与自动化')}</p>
<h1>{t('Fewer manual steps in the work that <em>slows your team down.</em>', '减少那些<em>拖慢团队的</em>手工环节')}</h1>
<p class="lede">{t('We map, build and run AI-assisted workflows for operations teams and online sellers. Remote-first, fixed-scope to start, with a person reviewing every exception.', '我们为运营团队和线上卖家梳理、搭建并运行 AI 辅助的工作流。远程交付，先从固定范围的评估开始，每个异常都由人来复核。')}</p>
<div class="actions"><a class="btn" href="{url(lang, 'contact')}">{t('Book a discovery call', '预约初步沟通')}</a>
<a class="btn ghost" href="{url(lang, 'demos')}">{t('Try the demos', '试用演示应用')}</a></div>
</div>
{ledger(t('Example · Supplier invoice intake', '示例 · 供应商发票处理'), t('Demo', '演示'), [
        (t('Invoice arrives by email', '发票通过邮件到达'), 'auto', t('auto', '自动')),
        (t('Fields extracted from the PDF', '从 PDF 中提取字段'), 'auto', t('auto', '自动')),
        (t('Matched to purchase order', '与采购订单匹配'), 'auto', t('auto', '自动')),
        (t('Mismatch flagged with reason', '不一致项标注原因'), 'human', t('review', '人工')),
        (t('Approved entry posted to ledger', '确认后的记录入账'), 'auto', t('auto', '自动'))],
        t('Illustrative flow. People handle exceptions; software handles the routine.', '示意流程：常规部分交给软件，异常交给人。'))}
</div></section>
<div class="strip"><div class="wrap">
<span>{t('California corporation', '加州公司')}</span><span>{t('Established 2016', '成立于 2016 年')}</span><span>{t('Remote delivery', '远程交付')}</span><span>{t('Fixed-scope start', '固定范围起步')}</span><span>{t('Human-reviewed', '人工复核')}</span>
</div></div>
"""
    sv = services_data(lang)
    svc = section(cards([(s['num'], s['title'], s['short'], s['bullets'], url(lang, 'services/' + s['slug']), t('Learn more →', '了解更多 →')) for s in sv]),
                  t('Services', '服务'), t('Three ways we help', '三类服务'),
                  t('Pick one, or start with an assessment and let the numbers decide where to begin.', '可以任选其一，也可以先做评估，再根据结果决定从哪里开始。'), 'tint')
    fitsec = section(fit(
        t('Where it helps', '适合的场景'),
        [t('High-volume, repetitive work', '量大且重复的工作'),
         t('Inputs that vary in format: PDFs, email, spreadsheets', '输入格式不一：PDF、邮件、表格'),
         t('Clear rules for what “correct” looks like', '“正确”有明确的规则'),
         t('Mistakes that a reviewer can catch', '出错后复核人员能发现')],
        t('Where it does not', '不适合的场景'),
        [t('Rare, one-off tasks', '罕见的一次性任务'),
         t('Decisions with no written criteria', '没有书面标准的决策'),
         t('Irreversible actions with no review step', '不可撤销且没有复核环节的操作'),
         t('Data that cannot be shared under any terms', '在任何条款下都不能共享的数据')]),
        t('Fit', '适用范围'), t('Where AI helps, and where it does not', 'AI 在哪里有用，在哪里没用'),
        t('We say so early when a process is not worth automating. It saves both of us time.', '如果某个流程不值得自动化，我们会尽早直说，这能节省双方的时间。'))
    dm = section(cards([(d['num'], d['title'], d['text'], None, url('en', 'demos/' + d['slug']), t('Try the demo →', '试用演示 →')) for d in demos_data(lang)]),
                 t('Demos', '演示应用'), t('Working demos you can try', '可以直接试用的演示'),
                 t('Small applications built on common scenarios with sample data. They run in your browser and upload nothing. They show the shape of the work, not client results.',
                   '基于常见场景、使用示例数据的小型应用，在浏览器中本地运行，不上传任何内容。它展示的是工作的形态，不是客户成果。'), 'tint')
    pr = section(cards([
        ('01', t('Measure first', '先度量'), t('We baseline the current process before changing it, so improvement is something you can check.', '改动之前先记录现状基线，让改进可以被验证。'), None, None, None),
        ('02', t('Review built in', '内置复核'), t('Exceptions and sensitive actions go to a person, with the reason attached.', '异常和敏感操作交给人处理，并附上原因。'), None, None, None),
        ('03', t('Reversible by design', '可撤回'), t('Every workflow has logging and a clear way to switch it off.', '每个流程都有日志，并有明确的关闭方式。'), None, None, None),
        ('04', t('Documented', '有文档'), t('What was built, what data it touches and how to run it, written down.', '做了什么、涉及哪些数据、如何运行，都有书面记录。'), None, None, None)], 4),
        t('Principles', '原则'), t('How we approach the work', '我们的做事方式'))
    st = section(steps([
        (t('Assess', '评估'), t('A short, fixed-scope review of one process: steps, volumes, error cases and who touches what.', '对一个流程做简短、范围固定的梳理：步骤、量级、出错情形，以及谁在经手。')),
        (t('Prototype', '原型'), t('A working version on real samples, so you judge results rather than slides.', '用真实样本做出可运行的版本，让你看结果，而不是看幻灯片。')),
        (t('Deploy', '上线'), t('Rolled out with human review on, logging on and a clear way to turn it off.', '开启人工复核与日志，并保留清晰的关闭方式。')),
        (t('Improve', '改进'), t('We review the exceptions together each month and tighten the rules.', '每月一起复盘异常案例，持续收紧规则。'))]) +
        '<p style="margin-top:32px"><a class="btn ghost" href="%s">%s</a></p>' % (url(lang, 'how-we-work'), t('See the full process', '查看完整流程')),
        t('Approach', '合作方式'), t('Small, measured, reversible', '小步、可衡量、可撤回'), '', 'tint')
    ins = section(cards([('', a['title'], a['desc'], None, url(lang, 'insights/' + a['slug']), t('Read →', '阅读 →')) for a in insights]),
                  t('Insights', '洞察'), t('Notes from the work', '实践笔记'))
    fq = faq_items(lang)
    faqsec = section(faq(fq), t('FAQ', '常见问题'), t('Common questions', '常见问题'), '', 'tint', narrow=True)
    body = hero + svc + fitsec + dm + pr + st + ins + faqsec + cta(lang)
    title = t('DXC Group Inc | AI Workflow Automation & Consulting', 'DXC Group Inc | AI 流程自动化与咨询服务')
    desc = t('DXC Group Inc is a California corporation (est. 2016) helping businesses automate complex workflows, cut e-commerce operating costs and adopt AI responsibly. Delivered remotely.',
             'DXC Group Inc 是一家 2016 年成立的加州公司，帮助企业自动化复杂流程、降低电商运营成本，并稳妥地引入 AI。全程远程交付。')
    return title, desc, body, graph(org_schema(), faq_schema(fq))


# ------------------------------------------------------------------ services hub

def services_hub(lang):
    t = mk(lang)
    sv = services_data(lang)
    body = page_hero(lang, [(t('Services', '服务'), None)], t('Services', '服务'),
                     t('Three service lines, one way of working: small scope first, results you can check, a person in the loop.',
                       '三条服务线，同一种工作方式：先从小范围开始，结果可验证，始终有人参与。'))
    body += section(cards([(s['num'], s['title'], s['short'], s['bullets'], url(lang, 'services/' + s['slug']), t('Learn more →', '了解更多 →')) for s in sv]), cls='')
    body += section(cards([
        (t('Assessment', '评估'), t('Fixed-scope assessment', '固定范围评估'), t('A short review of one process or one question, with a written findings document and a recommendation. A good first step when you are not sure where AI helps.', '针对一个流程或一个问题的简短评估，交付书面结论与建议。适合还不确定 AI 能帮在哪里的团队。'), None, None, None),
        (t('Project', '项目'), t('Build project', '搭建项目'), t('A defined piece of work, such as one automated workflow, delivered with documentation and a hand-over. Scope and price are agreed up front.', '一项明确的工作，例如一个自动化流程，附文档并完成交接。范围和价格事先约定。'), None, None, None),
        (t('Retainer', '订阅'), t('Monthly support', '月度支持'), t('Ongoing monitoring, exception review and improvements for workflows already in use.', '对已上线的流程持续监控、复盘异常并改进。'), None, None, None)], 3),
        t('Engagement models', '合作形式'), t('Three ways to work together', '三种合作形式'),
        t('Most clients start with an assessment. Nothing is bundled; you choose what you need.', '大多数客户从评估开始。不做捆绑，按需选择。'), 'tint')
    body += cta(lang)
    return (t('Services | DXC Group Inc', '服务 | DXC Group Inc'),
            t('AI workflow automation, e-commerce operations and AI adoption advisory from DXC Group Inc. Fixed-scope assessments, project builds and monthly support, delivered remotely.',
              'DXC Group Inc 提供 AI 流程自动化、电商运营与 AI 落地咨询。固定范围评估、项目搭建与月度支持，全程远程交付。'),
            body, graph(org_schema()))


# ------------------------------------------------------------------ service detail pages

def service_page(lang, slug, related_articles):
    t = mk(lang)
    D = {
        "workflow-automation": dict(
            title=t("Business workflow automation", "企业流程自动化"),
            lede=t("For teams whose work moves between inboxes, PDFs, spreadsheets and several systems, with people re-typing the same data at every step.",
                   "适合工作在邮箱、PDF、表格和多个系统之间流转、每一步都要人工重复录入的团队。"),
            problems=[t("Invoices and orders are keyed in by hand and checked against another system", "发票和订单靠手工录入，再与另一个系统核对"),
                      t("Emails and attachments are sorted by someone reading each one", "邮件和附件要靠人逐封阅读后分类"),
                      t("Month-end reconciliation depends on copying between spreadsheets", "月末对账依赖在多个表格之间复制数据"),
                      t("Errors are found late, and nobody can say where they started", "错误很晚才被发现，也说不清从哪一步开始")],
            build=[(t("Intake", "接收"), t("Read email, PDFs and forms and pull out the fields that matter.", "读取邮件、PDF 和表单，提取关键字段。")),
                   (t("Check", "校验"), t("Compare against purchase orders, price lists or master data and apply your rules.", "与采购订单、价目表或主数据比对，并应用你的规则。")),
                   (t("Route", "分派"), t("Send clean items straight through and exceptions to the right person with the reason.", "合格的直接通过，异常附上原因交给对应的人。")),
                   (t("Record", "留痕"), t("Post to your ERP, CRM or sheet and keep an audit log of what happened.", "写入 ERP、CRM 或表格，并保留完整的操作日志。"))],
            ledger_l=t("Example · Order intake", "示例 · 订单接收"),
            rows=[(t("Order arrives as PDF or email", "订单以 PDF 或邮件到达"), "auto", t("auto", "自动")),
                  (t("Customer, items and quantities extracted", "提取客户、商品和数量"), "auto", t("auto", "自动")),
                  (t("Checked against price list and stock", "与价目表和库存比对"), "auto", t("auto", "自动")),
                  (t("Unusual order held for approval", "异常订单挂起待审批"), "human", t("review", "人工")),
                  (t("Order entered in ERP", "订单录入 ERP"), "auto", t("auto", "自动"))],
            deliver=[t("Process map of the current workflow and its exception cases", "现有流程及其异常情形的流程图"),
                     t("Working automation connected to your systems, with review queue", "对接你系统的可运行自动化，含人工复核队列"),
                     t("Rules and prompts documented in plain language", "用平实语言记录的规则与提示词"),
                     t("Runbook: how to monitor, pause and roll back", "运行手册：如何监控、暂停与回退")],
            need=[t("A sample of real inputs, with sensitive details removed where possible", "一批真实输入样本，尽可能去除敏感信息"),
                  t("Someone who knows today’s process and its exceptions", "了解现有流程及其异常的负责人"),
                  t("Access to the target system, scoped to what is needed", "目标系统的访问权限，仅限所需范围")],
            limits=[t("It works best where rules can be written down. Judgement-heavy decisions stay with people.", "规则能写下来的地方效果最好，依赖判断的决策仍由人负责。"),
                    t("Inputs of very poor quality, such as illegible scans, will still need a person.", "质量很差的输入（如无法辨认的扫描件）仍然需要人工处理。")],
            demo="invoice-matching",
            faqs=[(t("How long does a first workflow take?", "第一个流程需要多久？"), t("It depends on the number of systems and exception cases. We scope it in the assessment and give you a written estimate before building.", "取决于涉及的系统数量和异常情形。我们会在评估阶段确定范围，并在开工前给你书面估算。")),
                  (t("Do you replace our ERP?", "你们会替换我们的 ERP 吗？"), t("No. We connect to the systems you already use and leave them as the source of truth.", "不会。我们对接你现有的系统，并让它们继续作为数据的权威来源。"))]),
        "ecommerce-operations": dict(
            title=t("E-commerce operations", "电商运营"),
            lede=t("For online sellers whose costs grow with every order: support tickets, product data, returns and the exceptions in between.",
                   "适合成本随订单数同步增长的线上卖家：客服工单、商品数据、退换货，以及其间的各种异常。"),
            problems=[t("Support agents answer the same ten questions all day", "客服一整天都在回答同样的十来个问题"),
                      t("Product titles, attributes and descriptions differ across channels", "商品标题、属性和描述在各个渠道不一致"),
                      t("Returns and refunds are handled case by case, with no playbook", "退换货和退款逐案处理，没有统一规范"),
                      t("Peak season means temporary hires and uneven quality", "旺季要临时招人，质量参差不齐")],
            build=[(t("Ticket triage", "工单分流"), t("Classify by intent and urgency, so urgent and billing issues surface first.", "按意图和紧急程度分类，让紧急问题和账单问题优先出现。")),
                   (t("Drafted replies", "回复草稿"), t("Draft answers from your policies and help articles, for an agent to edit and send.", "根据你的政策和帮助文档生成回复草稿，由客服修改后发送。")),
                   (t("Listing cleanup", "刊登整理"), t("Normalize titles, attributes and descriptions to your own style guide.", "按你自己的规范统一标题、属性和描述。")),
                   (t("Returns playbook", "退换货规范"), t("Turn case-by-case handling into clear rules with escalation paths.", "把逐案处理变成清晰的规则，并设定升级路径。"))],
            ledger_l=t("Example · Support inbox", "示例 · 客服收件箱"),
            rows=[(t("Message arrives", "消息到达"), "auto", t("auto", "自动")),
                  (t("Category and priority assigned", "分配类别与优先级"), "auto", t("auto", "自动")),
                  (t("Reply drafted from policy", "依据政策生成回复草稿"), "auto", t("auto", "自动")),
                  (t("Agent edits and approves", "客服修改并确认"), "human", t("review", "人工")),
                  (t("Reply sent, ticket logged", "发送回复并记录工单"), "auto", t("auto", "自动"))],
            deliver=[t("Review of ticket types and where time is spent", "工单类型与耗时分布的分析"),
                     t("Triage and draft-reply workflow in your help desk", "在你的客服系统中运行的分流与回复草稿流程"),
                     t("Style guide and cleanup rules for product data", "商品数据的规范与整理规则"),
                     t("Returns and exceptions playbook", "退换货与异常处理规范")],
            need=[t("An export of recent tickets, with customer details removed", "近期工单导出（去除客户信息）"),
                  t("Your policies for shipping, returns and refunds", "运费、退换货与退款政策"),
                  t("An agent or lead who can review drafts early on", "能在早期审阅草稿的客服或主管")],
            limits=[t("Replies are drafts. We do not recommend sending AI-written answers to customers without review.", "回复仅为草稿。我们不建议未经复核就把 AI 生成的回答发给客户。"),
                    t("Gains depend on how repetitive your tickets are. We measure that in the assessment first.", "效果取决于工单的重复程度，我们会先在评估阶段量化。")],
            demo="ticket-triage",
            faqs=[(t("Which help desks do you work with?", "支持哪些客服系统？"), t("We work with whatever you use, as long as it offers an export or an API. We confirm this in the assessment.", "只要提供导出或 API，我们就能配合。会在评估阶段确认。")),
                  (t("Can this run on our storefront platform?", "能在我们的店铺平台上运行吗？"), t("Usually yes, through its API or exports. Platform limits are checked up front.", "通常可以，通过其 API 或导出实现。平台的限制会事先核对。"))]),
        "ai-advisory": dict(
            title=t("AI adoption advisory", "AI 落地咨询"),
            lede=t("For leaders who are being asked about AI and want a practical answer: where it helps, what it costs and how to try it safely.",
                   "适合被问到“AI 怎么用”、想要一个务实答案的管理者：哪里有用、成本多少、怎样稳妥试点。"),
            problems=[t("Many ideas, no way to rank them", "想法很多，却没法排优先级"),
                      t("Vendor demos look the same and claims are hard to compare", "供应商演示大同小异，宣称的效果难以比较"),
                      t("Unclear who is responsible if an AI output is wrong", "AI 输出出错时，责任归谁并不清楚"),
                      t("Pilots that never reach daily use", "试点一直停留在试点阶段")],
            build=[(t("Use-case ranking", "场景排序"), t("List candidate uses and score them on value, effort, data readiness and risk.", "列出候选场景，按价值、投入、数据准备度和风险打分。")),
                   (t("Pilot roadmap", "试点路线图"), t("A small first pilot with a success measure, a time box and a stop rule.", "一个小型首个试点，含成功指标、时间盒与终止条件。")),
                   (t("Vendor and build review", "采购与自建评估"), t("Compare options against your needs, data terms and total cost.", "对照你的需求、数据条款和总成本比较各方案。")),
                   (t("Review and rollout rules", "复核与推广准则"), t("Who checks what, when to escalate and how to log decisions.", "谁检查什么、何时升级、如何记录决策。"))],
            ledger_l=t("Example · Use-case screen", "示例 · 场景筛选"),
            rows=[(t("List candidate use cases", "列出候选场景"), "human", t("workshop", "研讨")),
                  (t("Score value, effort, data, risk", "按价值、投入、数据、风险打分"), "human", t("workshop", "研讨")),
                  (t("Pick one pilot with a stop rule", "选定一个带终止条件的试点"), "human", t("decision", "决策")),
                  (t("Prototype on real samples", "用真实样本做原型"), "auto", t("build", "搭建")),
                  (t("Review results against the measure", "对照指标复盘结果"), "human", t("review", "复核"))],
            deliver=[t("Ranked list of use cases with the reasoning shown", "附评分依据的场景优先级清单"),
                     t("One-page pilot plan: scope, measure, timeline, owner", "一页纸试点计划：范围、指标、时间线、负责人"),
                     t("Vendor or build comparison where relevant", "必要时的供应商/自建对比"),
                     t("Draft review and escalation guidelines", "复核与升级准则草案")],
            need=[t("Time with the people who run the processes in question", "与相关流程负责人的沟通时间"),
                  t("A short description of your data and any constraints on sharing it", "对你的数据及共享限制的简要说明"),
                  t("A decision-maker for the pilot", "试点的决策人")],
            limits=[t("We give an independent view and will say when the answer is “not yet” or “not with AI”.", "我们提供独立意见，如果答案是“现在不适合”或“不必用 AI”，我们会直说。"),
                    t("Legal and compliance review of your use remains with your own counsel.", "针对你具体使用方式的法律与合规审查，仍应由你自己的律师负责。")],
            demo=None,
            faqs=[(t("Do you sell software or take vendor commissions?", "你们销售软件或收取供应商佣金吗？"), t("No. Advisory work is paid for by the client only, so recommendations are not tied to a product.", "不。咨询费用仅由客户支付，因此建议与任何产品无关。")),
                  (t("Is this only for large companies?", "只适合大公司吗？"), t("No. Smaller teams often benefit most, because one well-chosen pilot can change a lot.", "不是。小团队往往受益最大，因为一个选得好的试点就能带来很大改变。"))]),
    }[slug]
    sv = [s for s in services_data(lang) if s['slug'] == slug][0]
    hero = page_hero(lang, [(t('Services', '服务'), url(lang, 'services')), (D['title'], None)], D['title'], D['lede'])
    main_html = f"""<h2>{t('Typical problems', '常见问题')}</h2>{bullets(D['problems'])}
<h2>{t('What we build', '我们做什么')}</h2>"""
    main_html += "".join("<h3>%s</h3><p>%s</p>" % (a, b) for a, b in D['build'])
    main_html += f"<h2>{t('What you receive', '你会得到什么')}</h2>{bullets(D['deliver'])}"
    main_html += f"<h2>{t('What we need from you', '我们需要你提供')}</h2>{bullets(D['need'])}"
    main_html += f"<h2>{t('Limits', '局限')}</h2>{bullets(D['limits'])}"
    side = ledger(D['ledger_l'], t('Example', '示例'), D['rows'], t('Illustrative flow, not a client result.', '示意流程，并非客户成果。'))
    if D['demo']:
        dd = [d for d in demos_data(lang) if d['slug'] == D['demo']][0]
        side += ('<a class="card" href="%s"><span class="num">%s</span><h3>%s</h3><p>%s</p><span class="more">%s</span></a>' %
                 (url('en', 'demos/' + dd['slug']), dd['num'], dd['title'], dd['text'], t('Try the demo →', '试用演示 →')))
    side += '<a class="btn" href="%s">%s</a>' % (url(lang, 'contact'), t('Discuss your case', '聊聊你的情况'))
    body = hero + section('<div class="split"><div class="prose">%s</div><aside class="aside">%s</aside></div>' % (main_html, side), '', '', '', '')
    ra = [a for a in related_articles if slug in a['services']]
    if ra:
        body += section(cards([('', a['title'], a['desc'], None, url(lang, 'insights/' + a['slug']), t('Read →', '阅读 →')) for a in ra], 3),
                        t('Related reading', '相关阅读'), '', '', 'tint')
    body += section(faq(D['faqs']), t('FAQ', '常见问题'), t('Questions about this service', '关于该服务的常见问题'), '', '', narrow=True)
    body += cta(lang)
    title = t("%s | DXC Group Inc" % D['title'], "%s | DXC Group Inc" % D['title'])
    schema = graph(org_schema(), {
        "@type": "Service", "name": D['title'], "description": D['lede'],
        "provider": {"@id": BASE + "/#org"}, "areaServed": "US", "serviceType": D['title']},
        faq_schema(D['faqs']))
    return title, D['lede'], body, schema
