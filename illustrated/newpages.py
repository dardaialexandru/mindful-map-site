"""New sections: mind-body branches, emotions (pleasant / unpleasant), two new mind needs. Every claim comes from a source listed on its page."""
import schemes, icons

BR = "#5E7F5A"   # branches: mind-body
UN = "#8E4A5A"   # unpleasant emotions
PL = "#C79A3B"   # pleasant emotions
NEWCOL = {"recognition": "#9A5FA0", "creativity": "#2F8FA0"}

T = [
 dict(slug="breathing", dir="mindbody", name="Breathing", col=BR, ev="partial", evtext="Some evidence · small trials, moderate risk of bias", scheme="breathing",
  lede="Slow, steady breathing is one of the few things that link body and mind in both directions.",
  plain="When you breathe slowly, your heartbeat settles and your body gets the message that it is safe. That calm can then reach your mind. This is one of the clearest examples of the body talking to the mind.",
  says=["In 12 trials on stress, 20 on anxiety and 18 on depression, with 785 adults, breathing exercises were better than the control groups. The effects were small to medium.",
        "Breathing guided by a heart-rate sensor (heart-rate-variability biofeedback) lowered stress and anxiety by a large amount in 24 studies with 484 people.",
        "Most of the exercises were slow or abdominal breathing. Fast-paced breathwork was studied less, and its safety needs more research."],
  limits="Most trials had a moderate risk of bias and small groups. The benefit may come from the calm, focused attention, not from breathing itself. It may help some people and not others.",
  tryit=["Try breathing out a little longer than you breathe in, for a few minutes.", "If dizzy or unwell, stop. Avoid fast breathing exercises unless a professional guides you.", "If anxiety lasts for weeks, talk to a doctor. Breathing is an extra, not a replacement."],
  conn=[("mindbody/relaxation.html", "Relaxation", "Another way to reach the same calm."), ("emotion/calm.html", "Calm", "The feeling this practice is aimed at."), ("feel/tense.html", "Feeling: Tense or anxious", "Where breathing may help most."), ("mindbody/vagus.html", "Heart rhythm and calm", "The rhythm this practice acts on.")],
  src=["Fincham et al. 2023, Scientific Reports: effect of breathwork on stress and mental health (RCTs, 785 adults).", "Meta-analysis of heart-rate-variability biofeedback for stress and anxiety, Psychological Medicine (24 studies, 484 people)."]),
 dict(slug="relaxation", dir="mindbody", name="Relaxation", col=BR, ev="partial", evtext="Some evidence · medium effect on anxiety", scheme="relaxation",
  lede="Letting the muscles and the mind loosen, on purpose.",
  plain="Relaxation training teaches the body to let go of tension step by step. When the body is loose, the mind finds it harder to stay on edge.",
  says=["In a review of 27 studies, relaxation training eased anxiety by a medium amount. Compared with other groups the effect was 0.51 on a scale where 0.5 is medium.",
        "The effects were larger for meditation-based training, for volunteers, and for longer treatments."],
  limits="The review mixes proper trials with studies that had no comparison group, and it covers 1997 to 2007. Newer studies may differ. It is about anxiety, not every kind of distress.",
  tryit=["Try tensing and then letting go of one muscle group at a time, from your feet upwards.", "Pick one time of day and keep it short. Regular beats long.", "If it makes you more anxious, stop and talk to a professional."],
  conn=[("mindbody/breathing.html", "Breathing", "Slow breathing works through a similar path."), ("emotion/calm.html", "Calm", "What relaxation aims for."), ("feel/tense.html", "Feeling: Tense or anxious", "Where it has been tested most.")],
  src=["Manzoni et al. 2008, BMC Psychiatry: relaxation training for anxiety, a ten-year systematic review with meta-analysis (27 studies)."]),
 dict(slug="stress", dir="mindbody", name="Stress and the body's defences", col=BR, ev="partial", evtext="Solid link in studies · illness effect not shown", scheme="stress",
  lede="Short stress prepares the body. Stress that never ends wears it down.",
  plain="Your body answers a threat by getting ready. For a short time that helps your defences. When the threat does not go away, the same system starts to cost you.",
  says=["A review of 293 studies with 18,941 people found that short stress boosted fast, general defences, while longer stress gradually weakened the immune response.",
        "The most severe effects came from stress with no end that changes who you are or your role among people.",
        "Older adults and people who are already ill were more affected."],
  limits="The studies measured many different immune markers, and the review could not show that these changes make people ill more often. It covers research up to 2001.",
  tryit=["Look for the stress that has no end, and see if one part of it can be changed or shared.", "Rest and recovery count. They are not a reward.", "If stress is constant and heavy, speak to a doctor or therapist."],
  conn=[("mindbody/inflammation.html", "Inflammation and mood", "A second route from the body to the mind."), ("mindbody/breathing.html", "Breathing", "One way to settle the stress response."), ("need/stability.html", "Stability", "Money, work and home are common sources of long stress."), ("mindbody/hormones.html", "Hormones and signals", "Cortisol, the stress hormone, and what is over-sold.")],
  src=["Segerstrom and Miller 2004, Psychological Bulletin: psychological stress and the human immune system, a meta-analytic study of 30 years of inquiry (293 studies)."]),
 dict(slug="inflammation", dir="mindbody", name="Inflammation and mood", col=BR, ev="partial", evtext="Some evidence · applies to some people", scheme="inflammation",
  lede="For some people, a body in low-grade inflammation and a low mood travel together.",
  plain="Inflammation is the body's alarm. In some people with depression it stays a little raised. That does not mean it causes the depression in everyone. It is one possible route between body and mind.",
  says=["Across 37 studies, about 27 in 100 people with depression had clearly raised CRP, a blood marker of inflammation. About 58 in 100 had mildly raised CRP.",
        "In 36 trials, anti-inflammatory drugs lowered depression scores compared with placebo. The effect was larger when added to an antidepressant."],
  limits="All the drug trials were at high risk of bias, and infections were slightly more frequent. Raised inflammation is not found in most people with depression. This is early research, not advice to take anti-inflammatory drugs for mood.",
  tryit=["Nothing here is a treatment to start on your own.", "Sleep, movement and long-lasting stress are things that also touch the body's inflammation. They are covered on their own pages.", "If low mood lasts, talk to a doctor. Mention any ongoing physical illness."],
  conn=[("mindbody/stress.html", "Stress and the body's defences", "Long stress may feed inflammation."), ("need/sleep.html", "Sleep", "Poor sleep is a common companion."), ("feel/sad.html", "Feeling: Sad", "Where the question has been studied."), ("mindbody/gut.html", "Gut and mind", "Another body route, still early.")],
  src=["Osimo et al. 2019, Psychological Medicine: prevalence of low-grade inflammation in depression, a meta-analysis of CRP levels (37 studies).", "Köhler-Forsberg et al. 2019, Acta Psychiatrica Scandinavica: anti-inflammatory treatment for depression, meta-analysis (36 trials)."]),
 dict(slug="hormones", dir="mindbody", name="Hormones and signals", col=BR, ev="partial", evtext="Some evidence · small gaps, easily over-sold", scheme="hormones",
  lede="Hormones carry messages between body and mind. Some of the popular stories about them do not hold up.",
  plain="Hormones are chemical messengers. The stress hormone cortisol does differ a little in depression. But two famous stories, oxytocin as the love hormone and serotonin as the happiness chemical, are much weaker than they sound.",
  says=["Across 361 studies with 18,454 people, cortisol was higher in people with depression (0.60). In the better-made studies the gap was about half as big (0.33). ACTH, the signal that tells the glands to act, was a little higher (0.28). CRH, the first signal in the brain, was not different.",
        "Seven experiments with 481 people did not show that a nasal spray of oxytocin raises trust (effect 0.08, about zero). In 12 trials with 273 people with schizophrenia, it did not help social thinking overall.",
        "A 2022 review of reviews found no consistent proof that depression is caused by low serotonin. It did not test whether antidepressants work."],
  limits="Averages hide a lot. A hormone that is higher on average does not tell you what any one person has. The review of serotonin did not look at antidepressants, so it says nothing about stopping them. Do not stop a medicine without a doctor.",
  tryit=["Be wary of any product or post that promises to \"boost\" a hormone.", "Long stress, poor sleep and loneliness all touch these systems. They are covered on their own pages.", "If low mood lasts, talk to a doctor. Blood tests for hormones are not a way to diagnose depression."],
  conn=[("mindbody/stress.html", "Stress and the body's defences", "Cortisol is part of the stress response."), ("mindbody/inflammation.html", "Inflammation and mood", "Another body signal linked to mood."), ("need/touch.html", "Touch", "Often linked to oxytocin in popular stories. The studies of the spray do not show trust."), ("need/sleep.html", "Sleep", "Poor sleep is a common companion of raised stress hormones.")],
  src=["Stetler and Miller 2011, Psychosomatic Medicine: depression and hypothalamic-pituitary-adrenal activation, a quantitative summary of four decades of research (361 studies, 18,454 people).", "Nave, Camerer and McCullough 2015, Perspectives on Psychological Science: does oxytocin increase trust in humans? A critical review.", "Bürkner et al. 2017, Schizophrenia Bulletin: oxytocin for cognitive deficits in schizophrenia, meta-analysis (12 trials, 273 people).", "Moncrieff et al. 2022, Molecular Psychiatry: the serotonin theory of depression, a systematic umbrella review."]),
 dict(slug="vagus", dir="mindbody", name="Heart rhythm and calm", col=BR, ev="partial", evtext="Observed link · cause not shown", scheme="vagus",
  lede="The beat-to-beat rhythm of your heart carries a message about how settled your body is.",
  plain="A calm heart does not beat like a clock. It speeds up a little when you breathe in and slows when you breathe out. This small swing is called heart-rate variability. It is linked to the vagus nerve, the long nerve that links brain, heart and gut.",
  says=["In 36 studies, people with anxiety disorders had a lower heart-rate variability than people without (about 0.29 on the main measure, a small gap). It was larger in generalised anxiety (0.56) and social anxiety (0.47), but those rest on only three data sets each.",
        "Slow breathing guided by a heart-rate sensor lowered stress and anxiety by a large amount in 24 studies with 484 people. That is covered on the Breathing page."],
  limits="The studies measured people once, so they cannot tell whether anxiety lowers the rhythm or the reverse. Results differed a lot between studies, and some studies may be missing. Not every kind of measure showed the gap.",
  tryit=["Slow breathing, with a longer out-breath, is the safest way to work with this system.", "Do not buy a device to chase a number. The number is not a goal.", "Regular movement and good sleep are linked to a healthier rhythm. See their pages."],
  conn=[("mindbody/breathing.html", "Breathing", "The practice that works through this rhythm."), ("mindbody/relaxation.html", "Relaxation", "Another way to quiet the body."), ("feel/tense.html", "Feeling: Tense or anxious", "Where the link has been studied."), ("mindbody/regulation.html", "How you handle feelings", "Handling feelings and the body's calm go together.")],
  src=["Chalmers et al. 2014, Frontiers in Psychiatry: anxiety disorders are associated with reduced heart rate variability, a meta-analysis (36 studies).", "Meta-analysis of heart-rate-variability biofeedback for stress and anxiety, Psychological Medicine (24 studies, 484 people)."]),
 dict(slug="gut", dir="mindbody", name="Gut and mind", col=BR, ev="weak", evtext="Early evidence · few small studies", scheme="gut",
  lede="The gut and the brain talk to each other. For mood, the evidence is still early.",
  plain="Trillions of bacteria live in your gut, and the gut is wired to the brain. Scientists are asking whether they affect mood. So far the answer is a cautious maybe.",
  says=["A review of 16 studies found that people with depression had fewer of some gut bacteria (including Faecalibacterium) than people without. This came from 10 studies with 701 people.",
        "In 6 trials with 302 people, probiotics reduced depression symptoms more than control treatments. The range around the result was very wide."],
  limits="Few and small studies. Diet and medicines were not well controlled, so they could explain the bacteria differences. The probiotic trials differ in strain, dose and who took part. This is not yet a treatment.",
  tryit=["Eating a mix of plants and fibre is good for the gut and has other benefits. The Food page has more.", "Probiotics are not a replacement for treatment of depression.", "If your gut and your mood both trouble you, tell a doctor about both."],
  conn=[("need/food.html", "Food", "What you eat is the main thing that shapes gut bacteria."), ("mindbody/inflammation.html", "Inflammation and mood", "The gut and inflammation may be connected."), ("mindbody/stress.html", "Stress and the body's defences", "Stress also reaches the gut."), ("feel/sad.html", "Feeling: Sad", "Where this question has been studied.")],
  src=["Systematic review and meta-analysis of gut microbiota and major depressive disorder, 2020 (16 studies: 10 observational, 701 people, and 6 trials, 302 people)."]),
 dict(slug="regulation", dir="mindbody", name="How you handle feelings", col=BR, ev="partial", evtext="Solid link · mostly from short tests", scheme="regulation",
  lede="What you do with a feeling matters about as much as the feeling itself.",
  plain="Everyone has hard feelings. What differs is what they do next. Going over them again and again, avoiding them or pushing them down goes with more distress. Looking at them from another angle helps a bit more.",
  says=["A review of 114 studies, with 241 effects, found that ruminating had the strongest link with depression and anxiety. Avoiding, pushing down and problem solving had medium to large links. Accepting and seeing things differently had small to medium links.",
        "In short experiments, looking at a situation differently reduced the feeling by a small amount (0.36). Pushing it down did less (0.16) and distraction did nothing on average (0.00).",
        "Bodily changes, such as muscle tension in the face, were small and uneven, in 68 studies with 4,474 people. Acceptance of your own emotions went with less negative emotion under stress, and better health six months later, in three studies. This is covered on the Emotions page."],
  limits="Most of the experiments used students and short, mild tasks. A strategy that works in a lab may not help in real distress. The strong links are from people measured once, so we cannot tell what causes what. Distraction can still help to get through a moment.",
  tryit=["Notice when you are going over the same thought again and again. Naming it is the first step.", "Try asking: what else could this mean? Do it when you are calm, not in the worst moment.", "If low mood or anxiety lasts, therapy that teaches these skills has support. See Reappraisal and CBT."],
  conn=[("door/reappraisal.html", "Door: Reappraisal", "A practice built on seeing things differently."), ("door/mindfulness.html", "Door: Mindfulness", "A practice built on noticing and accepting."), ("emotions.html", "Emotions", "Where the same emotion can land differently."), ("emotion/anger.html", "Anger", "What you do with anger matters too."), ("mindbody/vagus.html", "Heart rhythm and calm", "The body side of the same story.")],
  src=["Aldao, Nolen-Hoeksema and Schweizer 2010, Clinical Psychology Review: emotion-regulation strategies across psychopathology, a meta-analytic review (114 studies).", "Webb, Miles and Sheeran 2012, Psychological Bulletin: effectiveness of emotion-regulation strategies, meta-analysis (figures as cited in later work).", "Zaehringer et al. 2020, Frontiers in Psychology: psychophysiological effects of emotion down-regulation, systematic review and meta-analysis (68 studies, 4,474 people).", "Ford et al. 2018, Journal of Personality and Social Psychology: the psychological health benefits of accepting negative emotions and thoughts."]),
 dict(slug="recognition", dir="need", name="Recognition", col=NEWCOL["recognition"], ev="partial", evtext="Observed link · cause not shown", scheme="recognition", kind="mind",
  lede="Being seen, respected and fairly rewarded for what you do.",
  plain="People need to feel their effort counts for something. When it is not noticed or fairly rewarded, it wears on the mind, even if the work itself is fine.",
  says=["In 8 studies that followed 84,963 employees, people with high effort and low reward at work had about one and a half times the risk of later depression.",
        "In a survey in 123 countries, respect, along with support, autonomy and mastery, went with more enjoyment of life, meaning more good feelings and fewer bad ones."],
  limits="Effort and reward were reported once, at the start, by the workers themselves. The study covers working people, not family or friendships. These are links, not proven causes.",
  tryit=["Notice where your effort goes unseen, and say so to someone who can change it.", "Give recognition to others on purpose. It costs little.", "If you are never recognised at work and it hurts, that is a real signal, not weakness."],
  conn=[("need/stability.html", "Stability", "Work is where this need is most often unmet."), ("need/competence.html", "Competence", "Feeling capable and being recognised go together."), ("need/belonging.html", "Belonging", "Respect from people you care about matters most.")],
  src=["Rugulies et al. 2017, Scandinavian Journal of Work, Environment and Health: effort-reward imbalance at work and risk of depressive disorders (8 prospective studies, 84,963 employees).", "Tay and Diener 2011, Journal of Personality and Social Psychology: needs and subjective well-being around the world (123 countries)."]),
 dict(slug="creativity", dir="need", name="Creativity and imagination", col=NEWCOL["creativity"], ev="partial", evtext="Some evidence · older adults, in groups", scheme="creativity", kind="mind",
  lede="Making something, and giving the mind room to play.",
  plain="Painting, dancing, singing or making things with others gives the mind something to do besides worry. It also puts you among people, which may be part of why it works.",
  says=["A review of 39 studies in 21 countries found that group arts activities reduced depression (3,360 people) and anxiety (949 people) in older adults. The results were similar for painting, dance and music.",
        "The gain was bigger for people in care homes than for people living in the community.",
        "Imagination training is different. In a trial of 150 adults with depression, online training to picture positive scenes was no better than a matched control task, although both groups improved."],
  limits="The arts review is about older adults and groups, so we do not know how much comes from the art and how much from the company. The imagination trial was one trial. Play and curiosity as needs have little direct research yet.",
  tryit=["Pick something you can do with other people, even badly.", "Keep it simple: a song, a drawing, a walk with a camera.", "Do not expect an exercise in imagination alone to lift mood. The evidence is not there."],
  conn=[("need/belonging.html", "Belonging", "Group activity may be part of the benefit."), ("need/competence.html", "Competence", "Making things gives a feeling of being capable."), ("door/music.html", "Try: Music", "A way into creative activity."), ("feel/sad.html", "Feeling: Sad", "Where creative groups have been studied.")],
  src=["Group arts interventions for depression and anxiety in older adults, systematic review and meta-analysis, 2025 (39 studies, 21 countries), as reported by Queen Mary University of London.", "Blackwell et al. 2015, Clinical Psychological Science: positive imagery cognitive bias modification as a web-based treatment for depressed adults, randomised trial (150 adults)."]),
 dict(slug="calm", dir="emotion", name="Calm", col=PL, ev="partial", evtext="Some evidence · ways to reach it are tested", scheme="calm", tone="pleasant",
  lede="The settled, unhurried state. Not an absence of feeling, but a body at ease.",
  plain="Calm is easier to reach than to describe. The body slows down and the mind follows. Several simple practices have been tested for it.",
  says=["Relaxation training eased anxiety by a medium amount in 27 studies.", "Slow breathing guided by a heart-rate sensor helped stress and anxiety by a large amount in 24 studies with 484 people.", "Breathing exercises alone helped by a small to medium amount in 785 adults."],
  limits="These studies measured relief of anxiety and stress. They do not measure calm itself as a lasting state. Groups were small, and many trials had a moderate risk of bias.",
  tryit=["Try a few minutes of slow breathing before something stressful.", "Make the same short practice part of a routine.", "If you cannot feel calm for weeks, a professional can help."],
  conn=[("mindbody/breathing.html", "Breathing", "The fastest route to calm that has been tested."), ("mindbody/relaxation.html", "Relaxation", "A slower, step-by-step route."), ("need/sleep.html", "Sleep", "Rested people find calm easier."), ("mindbody/vagus.html", "Heart rhythm and calm", "The body side of calm.")],
  src=["Manzoni et al. 2008, BMC Psychiatry: relaxation training for anxiety (27 studies).", "Meta-analysis of heart-rate-variability biofeedback for stress and anxiety, Psychological Medicine (24 studies).", "Fincham et al. 2023, Scientific Reports: breathwork meta-analysis (785 adults)."]),
 dict(slug="awe", dir="emotion", name="Awe", col=PL, ev="weak", evtext="Early evidence · measured in short experiments", scheme="awe", tone="pleasant",
  lede="The feeling of standing in front of something much bigger than you.",
  plain="Awe is what many people feel in front of a huge landscape, a night sky, a piece of music or an act of great courage. Researchers have started to test what it does.",
  says=["A review of 84 studies with 17,801 people found that experimentally triggered awe had measurable effects on how people feel, judge and behave.", "Images, videos, recalled moments and real places all worked. Awe worked in positive and threatening settings.", "Effects on the body have hardly been studied."],
  limits="The experiments are short. The abstract gives no effect size, and nobody knows yet how long the effects last or whether they help in daily life.",
  tryit=["Look for a place or a view that makes you feel small, in a good way.", "Share it with someone.", "Do not force it. It cannot be ordered."],
  conn=[("door/nature.html", "Try: Nature", "Real places were one of the triggers."), ("door/music.html", "Try: Music", "Music is a common source of awe."), ("need/meaning.html", "Meaning", "Awe may touch how you see yourself, but this is early.")],
  src=["Meta-analysis of experimentally induced awe, 2022 (84 studies, 17,801 participants)."]),
 dict(slug="joy", dir="emotion", name="Joy and good feelings", col=PL, ev="partial", evtext="Observed link · cause not shown", scheme="joy", tone="pleasant",
  lede="Feeling well, cheerful or glad, and whether it matters for the body.",
  plain="Good feelings are not a reward at the end. Studies of healthy people over many years find that those who report more well-being tend to live somewhat longer.",
  says=["A review of 90 studies with about 1.3 million healthy adults found that better subjective well-being went with a lower risk of dying (ratio 0.92).", "In a survey in 123 countries, meeting higher needs (support, respect, autonomy, mastery) went with more good feelings and fewer bad ones."],
  limits="The studies differ a lot from each other, and the authors found signs of publication bias. This is a link. Feeling well may also reflect better health to begin with.",
  tryit=["Look at which need on the map is thin for you. Good feelings often follow the need being met.", "Do not turn this into pressure to be cheerful. Neutral days are normal."],
  conn=[("need/control.html", "Control", "A higher need linked to more good feelings."), ("need/belonging.html", "Belonging", "People you feel close to."), ("need/recognition.html", "Recognition", "Respect from others.")],
  src=["Review of subjective well-being and mortality in healthy populations (90 studies, about 1.31 million participants), hazard ratio 0.92.", "Tay and Diener 2011, Journal of Personality and Social Psychology: needs and subjective well-being around the world."]),
 dict(slug="anger", dir="emotion", name="Anger", col=UN, ev="partial", evtext="Observed link · mostly explained by habits", scheme="anger", tone="unpleasant",
  lede="The heat that rises when something feels unfair or blocked.",
  plain="Anger is a signal, often that a limit was crossed. The studies we found look at what long-lasting anger does to the heart.",
  says=["A review of 25 studies of healthy people found that anger and hostility went with 19% more heart events over the following years. In 18 studies of people who already had heart disease, it was 24% more.",
        "The link was stronger in men than in women among healthy people.",
        "When the studies accounted for smoking, activity, weight, income and treatment, the link was no longer significant."],
  limits="Most of the link seems to run through habits that often go with anger. The review looks at long-lasting hostility, not at ordinary anger. It says nothing about whether anger is good or bad in itself.",
  tryit=["Notice what limit was crossed. The anger often points to it.", "Slow breathing lowers the heat in the moment.", "If anger is hurting people around you, a therapist can help. This is common and treatable."],
  conn=[("mindbody/breathing.html", "Breathing", "A tested way to bring the heat down."), ("mindbody/stress.html", "Stress and the body's defences", "Long anger is a long stress response."), ("feel/tense.html", "Feeling: Tense or anxious", "Often close to it."), ("mindbody/regulation.html", "How you handle feelings", "What you do with anger matters.")],
  src=["Chida and Steptoe 2009, Journal of the American College of Cardiology: anger and hostility and future coronary heart disease, a meta-analytic review of prospective evidence (25 healthy-population and 18 heart-disease studies)."]),
 dict(slug="grief", dir="emotion", name="Grief", col=UN, ev="partial", evtext="Some evidence · helps those who struggle most", scheme="grief", tone="unpleasant",
  lede="What losing someone, or something, does to a person.",
  plain="Grief is not an illness. Most people grieve and slowly find their way. For some, the loss stays stuck and help is useful.",
  says=["In 61 controlled studies of psychological help for bereaved people, the benefit right after was small and no longer significant at follow-up.",
        "Help aimed at people with marked difficulty adapting to the loss worked about as well as therapy for other problems.",
        "Help offered to everyone without screening for distress was weaker, because many of those in the comparison groups improved on their own."],
  limits="The abstract gives no exact effect size, and the review was published in 2008. Newer treatments for prolonged grief may do better. We have not covered them here.",
  tryit=["Let the loss take the time it takes. Ordinary grief does not need treatment.", "Keep one or two people close.", "If grief stays as strong after many months and stops you living, talk to a doctor or therapist."],
  conn=[("need/belonging.html", "Belonging", "People around you matter most in grief."), ("feel/lonely.html", "Feeling: Lonely", "Loss often brings loneliness."), ("feel/sad.html", "Feeling: Sad", "Often part of grief."), ("mindbody/regulation.html", "How you handle feelings", "How people cope with hard feelings.")],
  src=["Currier, Neimeyer and Berman 2008, Psychological Bulletin: the effectiveness of psychotherapeutic interventions for bereaved persons, a comprehensive quantitative review (61 studies)."]),
]
BYSLUG = {t["slug"]: t for t in T}

def _lede_tone(t): return {"pleasant": "Pleasant emotion", "unpleasant": "Unpleasant emotion"}.get(t.get("tone"), "Mind and body" if t["dir"] == "mindbody" else "Mind need")

def topic_page(t, G):
    header, footer, tint, dark, ev = G["header"], G["footer"], G["tint"], G["dark"], G["ev"]
    a = t["col"]; d = dark(a, .5)
    says = "".join(f"<p>{p}</p>" for p in t["says"]); tryli = "".join(f"<li>{x}</li>" for x in t["tryit"])
    cl = "".join(f'<li><a href="../{h}"><b>{n}</b></a><br>{x}</li>' for h, n, x in t["conn"])
    src = "".join(f"<li>{s}</li>" for s in t["src"])
    back = {"mindbody": ('../mindbody.html', "All mind–body links"), "emotion": ("../emotions.html", "All emotions"), "need": ("../index.html#needs", "All needs")}[t["dir"]]
    evc = {"solid": "", "partial": "partial", "weak": "weak"}[t["ev"]]
    return header("../", "") + f"""
<main class="page np" style="--a:{a};--t:{tint(a)};--d:{d}"><div class="band"><div class="wrap">
<div class="bt"><a class="crumb" href="{back[0]}">← {back[1]}</a>
<p class="tag">{_lede_tone(t)}</p>
<h1><span class="hi">{icons.ico(t["slug"], a, 34)}</span>{t["name"]}</h1>
<p class="lede">{t["lede"]}</p>
<div style="margin:16px 0 0"><span class="ev {evc}">{t["evtext"]}</span></div></div>
</div></div><div class="wrap body">
<figure class="glance"><figcaption><b>At a glance</b></figcaption>{schemes.fig(t["scheme"], a, d)}</figure>
<h2>In plain words</h2><p>{t["plain"]}</p>
<h2>What research says</h2>{says}
<div class="limits"><b>How far to trust it</b>{t["limits"]}</div>
<div class="tryit"><h2>What you can try</h2><ul>{tryli}</ul></div>
<h2>How it connects</h2><ul class="cl">{cl}</ul>
<p class="aster">What helps one person may not help another. This page is not medical advice.</p>
<div class="sources"><b>Sources</b><ul>{src}</ul></div>
</div></main>
{footer("../")}"""

def hub(G, kind):
    header, footer, tint, dark, ev = G["header"], G["footer"], G["tint"], G["dark"], G["ev"]
    def card(t):
        a = t["col"]; evc = {"solid": "", "partial": "partial", "weak": "weak"}[t["ev"]]
        return f'<li class="hubc" style="--c:{a}"><a href="{t["dir"]}/{t["slug"]}.html"><b>{icons.ico(t["slug"], a, 22)}{t["name"]}</b><span class="ev {evc}">{t["evtext"]}</span><span class="s">{t["lede"]}</span></a></li>'
    css = '<style>.hubc{list-style:none;margin:0 0 12px}.hubc a{display:block;padding:14px 16px;border:1px solid var(--line);border-left:6px solid var(--c);border-radius:14px;background:var(--card);text-decoration:none;color:var(--ink)}.hubc b{display:block;font-size:1.05rem}.hubc .s{display:block;margin-top:6px;color:var(--soft);font-size:.95rem}.hubs{padding:0;margin:8px 0 22px}.hubcols{display:grid;grid-template-columns:1fr 1fr;gap:24px}@media(max-width:720px){.hubcols{grid-template-columns:1fr}}</style>'
    if kind == "mindbody":
        items = "".join(card(t) for t in T if t["dir"] == "mindbody")
        body = f"""<p class="tag">Branches of the tree</p><h1>Mind and body talk to each other</h1>
<p class="lede">On the tree, the branches carry messages between the trunk (the body) and the crown (the mind). Here are the routes that research has tested.</p>
<ul class="hubs">{items}</ul>
<div class="limits"><b>How far to trust it</b>None of these is a cure, and several rest on small or early studies. Each page says how sure we are. Interoception, the sense of your own body, is on the list to research. It is not here yet because we have not found enough solid studies.</div>"""
    else:
        un = "".join(card(t) for t in T if t.get("tone") == "unpleasant"); pl = "".join(card(t) for t in T if t.get("tone") == "pleasant")
        body = f"""<p class="tag">Emotions</p><h1>Emotions: pleasant and unpleasant</h1>
<p class="lede">An emotion is the reaction of your body and mind. A feeling is what you notice and name. Researchers do not all agree on this split, so we use it only as a simple lens. Feelings sit on their own pages, as signals that a need may be unmet.</p>
<div class="hubcols"><div><h2>Pleasant</h2><ul class="hubs">{pl}</ul></div><div><h2>Unpleasant</h2><ul class="hubs">{un}</ul></div></div>
<h2>The same emotion can land differently</h2>
<p>Pleasant and unpleasant describe how an emotion feels, not whether it is good or bad for you. How you read it changes what it does.</p>
<figure class="glance"><figcaption><b>At a glance</b></figcaption>{schemes.fig("mixed", "#8E4A5A", "#4A2530")}</figure>
<div class="limits"><b>How far to trust it</b>These are links from a few studies and one large survey. We have only a few emotions here so far. Fear, shame, guilt, hope and others are still being researched and are not on the map yet.</div>
<div class="sources"><b>Sources</b><ul><li>Ford et al. 2018, Journal of Personality and Social Psychology: the psychological health benefits of accepting negative emotions and thoughts, laboratory, diary and longitudinal evidence (three studies).</li><li>Quoidbach et al. 2014, Psychological Science: emodiversity and the emotional ecosystem (35,800 and 1,273 people).</li><li>Tay and Diener 2011, Journal of Personality and Social Psychology: needs and subjective well-being around the world (123 countries).</li></ul></div>"""
    return header("", "") + css + f'<main class="page np" style="--a:{BR if kind=="mindbody" else UN};--t:{tint(BR if kind=="mindbody" else UN)};--d:{dark(BR if kind=="mindbody" else UN,.5)}"><div class="wrap solo body" style="padding-top:34px">{body}</div></main>' + footer("")

def build(G):
    out = {}
    for t in T:
        out[f'{t["dir"]}/{t["slug"]}.html'] = (f'{t["name"]} | The Mindful Map', t["lede"], topic_page(t, G), "../")
    out["mindbody.html"] = ("Mind and body | The Mindful Map", "The routes that link body and mind, and what research says about each.", hub(G, "mindbody"), "")
    out["emotions.html"] = ("Emotions | The Mindful Map", "Pleasant and unpleasant emotions, and what research says about each.", hub(G, "emotions"), "")
    return out

def patch_index(body):
    li = lambda s, n, e, lede, c: f'<li><a href="need/{s}.html"><b>{icons.ico(s, c, 20)}{n}</b><span class="ev partial">{e}</span><span class="s">{lede}</span></a></li>'
    extra = li("recognition", "Recognition", "Observed link · cause not shown", "Being seen and fairly rewarded.", NEWCOL["recognition"]) + li("creativity", "Creativity and imagination", "Some evidence · older adults, in groups", "Making things, with other people.", NEWCOL["creativity"])
    body = body.replace('</ul>\n<details class="aster">', extra + '</ul>\n<details class="aster">', 1)
    body = body.replace("Crown: 5 needs of the mind", "Crown: 7 needs of the mind").replace("The twelve needs", "The fourteen needs").replace("Twelve needs, twelve colors. Tap one to jump in.", "Fourteen needs, each with its own sign. Tap one to jump in.")
    body = body.replace('</ul><p class="palcap">', "".join(f'<li><a href="need/{s}.html" style="background:{c}" title="{nm}" aria-label="{nm}"></a></li>' for s, nm, c in [("recognition", "Recognition", NEWCOL["recognition"]), ("creativity", "Creativity", NEWCOL["creativity"])]) + '</ul><p class="palcap">', 1)
    # mobile list under the tree (labels are hidden there): new needs, branches, emotions, in tree order
    _mi = lambda d, t: f'<li><a href="{d}/{t["slug"]}.html">{icons.ico(t["slug"], t["col"], 16)}{t["name"]}</a></li>'
    _newmind = "".join(f'<li><a href="need/{s}.html">{icons.ico(s, c, 16)}{nm}</a></li>' for s, nm, c in [("recognition", "Recognition", NEWCOL["recognition"]), ("creativity", "Creativity", NEWCOL["creativity"])])
    _mb = '<h3>Mind and body (branches)</h3><ul>' + "".join(_mi("mindbody", t) for t in T if t["dir"] == "mindbody") + '</ul><h3>Emotions</h3><ul>' + "".join(_mi("emotion", t) for t in T if t["dir"] == "emotion") + '</ul>'
    _k = body.index('<h3>Needs of the mind</h3><ul>'); _e = body.index('</ul>', _k)
    body = body[:_e] + _newmind + '</ul>' + _mb + body[_e + 5:]
    body = body.replace("Twelve needs: seven for the body, five for the mind.", "Fourteen needs: seven for the body, seven for the mind.")
    sect = """<section class="block" id="mindbody"><div class="wrap"><h2>The branches and the emotions</h2>
<p class="lede">Two more parts of the map. The branches are the routes between body and mind. Emotions are neither body nor mind alone, and they come pleasant and unpleasant.</p>
<div class="cols"><div><div class="colhead"><i style="background:#5E7F5A"></i>Mind and body</div><div class="colsub">The branches of the tree</div><ul class="needs">""" + "".join(f'<li><a href="mindbody/{t["slug"]}.html"><b>{icons.ico(t["slug"], t["col"], 20)}{t["name"]}</b><span class="ev partial">{t["evtext"]}</span><span class="s">{t["lede"]}</span></a></li>' for t in T if t["dir"] == "mindbody") + """</ul><p class="note"><a href="mindbody.html"><b>All mind–body links →</b></a></p></div>
<div><div class="colhead"><i style="background:#C79A3B"></i>Emotions</div><div class="colsub">Pleasant and unpleasant</div><ul class="needs">""" + "".join(f'<li><a href="emotion/{t["slug"]}.html"><b>{icons.ico(t["slug"], t["col"], 20)}{t["name"]}</b><span class="ev {"weak" if t["ev"]=="weak" else "partial"}">{t["evtext"]}</span><span class="s">{t["lede"]}</span></a></li>' for t in T if t["dir"] == "emotion") + """</ul><p class="note"><a href="emotions.html"><b>All emotions, pleasant and unpleasant →</b></a></p></div></div></div></section>
"""
    return body.replace('<section class="block" id="how">', sect + '<section class="block" id="how">', 1)
