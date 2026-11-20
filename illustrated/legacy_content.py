# -*- coding: utf-8 -*-
# All site content (English original). Evidence: good / medium / limited. kind: helps (shown in trials) / link (observed link only)
SITE = "The Mindful Map"
FEELINGS = [
 ("tired","Tired","Low on energy, heavy, drained.",["sleep","movement","rhythm-light","food"],
  "If tiredness lasts for weeks, ask a doctor. Thyroid problems, anemia and other medical causes are common and treatable."),
 ("tense","Tense or anxious","On edge, racing thoughts, tight body.",["sleep","movement","control","touch"],None),
 ("sad","Sad","Low mood, flat, no pleasure in things.",["belonging","movement","sleep","meaning"],
  "If low mood is deep and lasts more than two weeks, talk to a doctor or therapist. That is true whatever label you give it."),
 ("lonely","Lonely","Far from people, or alone among them.",["belonging","touch","meaning"],None),
 ("stuck","Stuck","Not moving forward, no way to decide.",["control","competence","movement"],None),
 ("pointless","Without purpose","Life feels like it has no point.",["meaning","belonging","competence"],None),
 ("pain","Pain","Aching or tension that will not go away.",["movement","sleep","touch"],
  "See a doctor if pain is new, severe, or comes with other symptoms. Do not stop or change a medicine without talking to your doctor. For long-lasting pain, see Life around you."),
]
NEEDS = [
 # slug, group, title, one-line, level, kind, body paragraphs, try list
 ("sleep","body","Sleep","Enough, and at regular hours.","good","helps",
  ["Too little sleep raises anxiety and dulls good feelings. Its effect on low mood is less clear-cut. The link with anxiety is among the best supported on the map. Irregular sleep timing is also linked with a higher risk of early death in a large study, but that is an observed link only.",
   "Regular hours matter as much as total hours: going to bed and getting up at similar times each day."],
  ["Keep a fixed wake-up time, including weekends.","Get daylight in the morning.","If you cannot sleep for weeks, talk to a doctor."]),
 ("movement","body","Movement","Walking, strength, anything that raises your pulse.","good","helps",
  ["In trials, exercise eases depression by a moderate amount, though many trials were small and the evidence is not strong. It seems to work about as well as talking therapy; the comparison with medicine rests on few small trials.",
   "It is not a cure and it does not replace treatment. It is one of the few things that helps almost everyone a little."],
  ["Start small: a ten-minute walk counts.","Pick something you will repeat, not something heroic.","Habits take months to settle, not three weeks."]),
 ("food","body","Food","What and how you eat.","medium","link",
  ["People who eat a lot of ultra-processed food have more anxiety and depression. That is a link only: we do not know which causes which.",
   "One small trial found that help to eat better lifted mood in people with depression, but it was too small to be sure."],
  ["Regular meals, mostly unprocessed food.","Do not treat food as a cure for low mood."]),
 ("rhythm-light","body","Rhythm and light","Regular days and daylight, especially in the morning.","limited","link",
  ["Body clocks like regularity. Morning daylight probably helps sleep and mood, but the evidence is thin to medium.",
   "In some trials, a bright-light lamp used alongside usual treatment helped people with depression. Guidelines still call the evidence uncertain, so treat it as an extra, not a replacement."],
  ["Go outside within an hour of waking.","Keep meal and sleep times regular."]),
 ("touch","body","Touch","Wanted, and often.","medium","link",
  ["In studies, touch such as massage or hugs lowers pain, anxiety and low mood. The studies are small and cannot be blinded, so the effect may be overstated. One study linked hugs with fewer colds, but it is a single study, and hugs may simply be a sign of good support.",
   "Touch is a need, not a treatment."],
  ["Ask for what you want from people you trust.","Pets, massage and close friends all count."]),
 ("safe-place","body","A safe place","Clean air, quiet, green space.","limited","link",
  ["Aircraft noise and pollution are linked with more depression. Green space and quiet are linked with better wellbeing. The evidence is thin to medium."],
  ["Spend time in green space when you can.","Reduce noise where you sleep."]),
 ("intimacy","body","Intimacy and reproduction","Closeness, sex, and children for those who want them.","medium","link",
  ["Sexual satisfaction goes with better wellbeing, but it is a link, not a proven cause. In the couples studied, the benefit rises up to about once a week and then levels off. This is not a target.",
   "Studies of whether having children makes people happier give mixed answers. On average the difference is small, and it depends on things like country, age and money.",
   "Anxiety or low mood before fertility treatment does not seem to lower the chance of pregnancy, so nobody should blame themselves."],
  ["Talk openly with a partner about needs.","See a doctor for fertility questions."]),
 ("control","mind","Control","Being able to decide about your own life.","good","link",
  ["People with more say over their lives do better. The link is strong, but we cannot be sure which causes which."],
  ["Make one small decision that is only yours today.","Change one thing you can change."]),
 ("competence","mind","Competence","Feeling capable.","good","link",
  ["Feeling able to do things goes with better wellbeing. Learning something and finishing it builds this."],
  ["Pick a small skill and practise it.","Plan with “if this, then I do that”. This works modestly in trials."]),
 ("belonging","mind","Belonging","People you feel close to.","medium","link",
  ["Warm and varied ties (friends, family, groups) go with better health. In large reviews, people with stronger social ties were about 50% more likely to survive the years studied. This is an observed link, not proof of cause, and marriage itself is not the key.",
   "Loneliness goes with poorer health and shorter life, but this is a link, not proof of cause.",
   "For loneliness, face-to-face groups and approaches that change how you think about relationships help in the short term, with low certainty.",
   "Couple therapy helps unhappy couples. Short courses give small to moderate gains, mostly to couples who are already somewhat unhappy."],
  ["Join one group that meets in person.","Contact one person you have lost touch with."]),
 ("meaning","mind","Meaning","Feeling that life has a point.","medium","link",
  ["A sense of purpose goes with better wellbeing and longer life in studies that only observe people. It is not proven that purpose adds years, and meaning is not yet a recommended treatment."],
  ["Ask what matters to you, and write down three answers.","Do one thing this week that follows from them."]),
 ("stability","mind","Stability","Money, work and a place to live.","good","link",
  ["Unemployment goes with worse mental health. Working 55 or more hours a week goes with a higher risk of stroke and, to a smaller degree, heart disease. Money helps, but only a little.",
   "Burnout is a work-related state, not a medical diagnosis, and its symptoms can look like those of depression. Programmes that change the work, and programmes that build personal skills, each give small gains in studies, mostly of health workers. The evidence is weak."],
  ["If work is wearing you down, change what you can in the work itself.","If low mood is deep and lasting, ask for a clinical check."]),
]
LEVELS = {"good":"Good evidence","medium":"Medium evidence","limited":"Limited evidence"}
KINDS = {"helps":"Shown to help in trials","link":"Observed link only"}

# ---- Doors: things you can try. (slug, group, title, one-line, level, kind, paragraphs, how, needs)
DOORS = [
 ("reappraisal","mind","Seeing a situation differently","Changing how you read what happened.","medium","helps",
  ["How you interpret a situation changes, by a moderate amount, how it affects you. This is the idea behind a lot of therapy."],
  ["Write down what happened, then two other ways to read it.","Ask what you would say to a friend in the same spot."],["control","competence"]),
 ("mindfulness","mind","Mindfulness","Paying attention to the present, without judging.","medium","helps",
  ["Mindfulness helps. In reviews it works about as well as other proven treatments such as therapy, though it is not better."],
  ["Start with five minutes of noticing your breath.","If it makes you feel worse, stop and talk to a professional."],["control"]),
 ("cbt","mind","Cognitive behavioural therapy","A structured talking therapy with a trained therapist.","good","helps",
  ["Good evidence that it helps with depression and anxiety. Its benefit looks smaller in the best-designed trials than in earlier, weaker ones."],
  ["Ask a doctor for a referral.","Look for a therapist trained in it."],["competence","control"]),
 ("gratitude","mind","Gratitude","Noticing and writing down what went well.","medium","helps",
  ["A small effect, mostly on good feelings. It was not the same in every country studied."],
  ["Write three good things at the end of the day, for a few weeks."],["meaning"]),
 ("kindness","mind","Acts of kindness","Doing something good for someone else.","medium","helps",
  ["Doing kind things for others gives the giver a small to medium lift in wellbeing."],
  ["Do one small kind thing a day for a week.","Choose things you would actually enjoy doing."],["belonging","meaning"]),
 ("exercise","body","Exercise","Aerobic and strength training.","good","helps",
  ["In trials, exercise helps depression by a moderate amount. We do not say it works as well as medicine; that comparison is uncertain."],
  ["Walk briskly 30 minutes, three times a week.","Add two short strength sessions."],["movement","competence"]),
 ("regular-sleep","body","Regular sleep","Same bedtime and wake-up time.","good","helps",
  ["Regular hours are one of the best-supported habits on the map."],
  ["Fix the wake-up time first.","No screens in bed if you can manage it."],["sleep"]),
 ("morning-light","body","Morning light","Daylight soon after waking.","limited","link",
  ["Evidence is thin to medium for daylight. In some trials a bright-light lamp used alongside usual treatment helped people with depression, but guidelines call the evidence uncertain. Blue-light glasses probably do not help sleep."],
  ["Spend ten minutes outside after waking."],["rhythm-light","sleep"]),
 ("wanted-touch","body","Wanted touch","Hugs, massage, closeness you want.","medium","link",
  ["In studies, touch such as massage or hugs lowers pain, anxiety and low mood, though the studies are small. Do not expect it to prevent illness."],
  ["Ask for a hug from someone you trust."],["touch","belonging"]),
 ("nature","body","Time in nature","Parks, woods, water.","medium","link",
  ["People who live near more green space have somewhat less depression and anxiety. This is a link, and we cannot be sure it is cause and effect."],
  ["Walk somewhere green once a week."],["safe-place","movement"]),
 ("music","body","Music","Listening or making it.","medium","helps",
  ["Music lowers felt stress by a medium amount, and has a smaller effect on pulse, blood pressure and stress hormones."],
  ["Make a playlist for winding down."],["safe-place"]),
 ("breathing","body","Conscious breathing","Slow, steady breaths.","medium","helps",
  ["Small to medium effect on stress and anxiety. No single technique has been shown to be better than another, and results mostly rely on what people say about themselves. Slow breathing also measurably changes heart rate variability, which reflects calmer nerve activity."],
  ["Breathe out a little longer than you breathe in for a few minutes."],["sleep","control"]),
]
# ---- How mind and body connect
LINKS = [
 ("Breathing and nerves","Slow breathing calms the body and raises heart rate variability. No technique is proven better than another.","medium","helps"),
 ("Stress hormones","Long-term stress changes the daily rhythm of stress hormones.","good","link"),
 ("Inflammation","In some people with depression there is mild inflammation. We do not know which causes which.","medium","link"),
 ("The gut","A link with mood is plausible, but the evidence is limited. Probiotics are not a proven treatment.","limited","link"),
 ("Repeating thoughts","Rumination and heavy worry raise pulse, blood pressure and stress hormones.","good","link"),
]
# ---- Background
BACKGROUND = [
 ("Heredity","Genes explain about a third of the differences in wellbeing. The rest comes from life experiences and surroundings. Genes load the dice; they do not decide alone.","good","link"),
 ("Childhood","A hard childhood raises the risk of depression in adulthood. This comes from memory and observation, not from experiments. The idea that trauma is “written in your DNA” has not held up.","good","link"),
 ("Surroundings","Aircraft noise and pollution are linked with more depression.","limited","link"),
 ("Personality","People who are more organised and conscientious live somewhat longer, on average. It is an observed link.","medium","link"),
]
STAGES = [
 ("All adults","Daily hormone rhythms, sleep, stress and body weight matter at every age."),
 ("Women","The cycle (mild changes for most, serious symptoms for some), pregnancy and the months after birth (talk to a doctor if low mood lasts), perimenopause (more depressive symptoms; clinical depression is less clear), and after menopause (unclear)."),
 ("Men","Testosterone follows a daily rhythm, and one small study found that a week of short sleep lowered it. There is no monthly cycle."),
 ("Older adults","About 45% (nearly half) of dementia cases could in theory be prevented or delayed by dealing with 14 factors, such as high blood pressure, smoking, lack of exercise, hearing loss and social isolation. The estimate assumes each link is largely causal, which is not certain, and it guarantees nothing for any one person."),
]
# ---- Life topics
LIFE = [
 ("Relationships","Warm, varied ties go with better health, but this is an observed link, not proof of cause. Couple therapy helps unhappy couples; short courses give small to moderate gains. For loneliness, face-to-face groups help in the short term. About two in three people who divorce show no lasting depression; roughly one in ten develops new depression and needs support.","medium","link"),
 ("Work","Burnout is a work-related state, not a medical diagnosis, and its symptoms can look like those of depression. Changing the work and building skills each give small gains, with weak evidence. Unemployment goes with worse mental health. Working 55 or more hours a week goes with a higher risk of stroke and, to a smaller degree, heart disease. Working from home depends on choice, amount and support. Job insecurity goes with worse mental health in long-term studies. Shift work goes with more heart attacks and diabetes, in observational studies only. Mindfulness at work helped stress, anxiety and sleep in trials; its effect on burnout is unclear.","medium","link"),
 ("Habits","A new habit takes months, not three weeks. Tracking your progress and “if this, then that” plans help by a small to medium amount. Plan for the days you miss.","medium","helps"),
 ("Trauma","Hard events are very common. PTSD is much rarer. Many people recover, and a notable share of cases ease within months. UK guidelines recommend trauma-focused therapy (CBT or EMDR) with a specialist for adults with PTSD. They advise against one-off “debriefing” right after an event, because trials found no benefit and one found a higher risk of PTSD. This site does not give therapy steps.","good","helps"),
 ("Screens and social media","The links with wellbeing are small and uneven, and most research is on teenagers. In adults, trials of cutting back on social media give conflicting results: one review found a small benefit, another found none. Breaks may need to last about a week or more to help. The US Surgeon General’s 2023 advisory is about young people and says the evidence is not yet enough to judge safety.","limited","helps"),
 ("Racing thoughts and ADHD","Racing or looping thoughts are not on the official list of ADHD symptoms. They can come from anxiety, low mood, stress, poor sleep or ADHD, so an assessment has to rule the others out. In adults, ADHD needs at least five symptoms, several of which started before age 12, and a specialist diagnosis. UK guidance recommends medication for some people and a structured psychological programme, which may include CBT.","medium","link"),
 ("Long-lasting pain","Exercise and CBT-based talking therapy help some people. Exercise gives small to moderate gains in moving and often eases pain a little, but trials were small, so we are not very sure. CBT changes pain itself very little, but gives small, reliable gains in distress and coping. UK guidance for long-lasting pain with no clear cause, read through summaries, recommends supervised group exercise and advises against starting several common painkillers, including opioids. Do not stop a medicine without talking to your doctor. About half of people with depression also report long-lasting pain, and the link runs both ways.","medium","helps"),
 ("Long-term illness and mood","Low mood and anxiety are common with long-term illness such as cancer, diabetes, heart disease and long COVID, and they can be treated. How common varies a lot between studies. In one trial of people with diabetes or heart disease, organised team care (doctor, nurse and follow-up) eased depression modestly. Tell your doctor if your mood changes.","limited","link"),
 ("Autism in adults","Many autistic adults have never been diagnosed, especially older adults. Hiding autistic traits to fit in goes with worse mental health. Anxiety and depression are common. UK guidance recommends assessment for adults, and supports such as group social learning, supported employment and CBT adapted to be concrete and structured. Autism is not an illness.","limited","link"),
 ("Grief, alcohol and meaning","Grief is normal. For a minority, roughly one in ten or fewer, it becomes a long-lasting illness. Drinking more goes with a higher risk of depression, and some studies suggest it may contribute, but the cause is uncertain. Alcohol also worsens sleep and mood.","medium","link"),
]

# ---- Sources actually opened during independent verification (8 Nov 2026).
# (label, url, note) note: "abstract", "press report", "manuscript", "guideline" etc.
SRC = {
 "sleep":[("Palmer et al. 2024, 154 sleep-loss experiments","https://pubmed.ncbi.nlm.nih.gov/38127505/","abstract")],
 "exercise":[("Cochrane review 2026, exercise for depression (73 trials)","https://knowledge.lancashire.ac.uk/id/eprint/57257/","abstract copy")],
 "food":[("Meta-analysis of 17 studies, ultra-processed food and depression/anxiety","https://researchonline.jcu.edu.au/76500/","abstract")],
 "light":[("Bright-light add-on, JAMA Psychiatry meta-analysis (press report)","https://www.psypost.org/bright-light-therapy-accelerates-treatment-response-in-nonseasonal-depression/","press report"),
          ("Golden et al. 2005, light therapy for depression","https://ajp.psychiatryonline.org/doi/abs/10.1176/appi.ajp.162.4.656","abstract"),
          ("NICE NG222, depression in adults","https://www.nice.org.uk/guidance/ng222/resources/depression-in-adults-treatment-and-management-pdf-66143832307909","guideline"),
          ("Cochrane 2023, blue-light filtering glasses (summary)","https://www.aop.org.uk/ot/news/2023/08/18/cochrane-review-on-blue-light-filtering-spectacles-published","summary")],
 "touch":[("Packheiser et al. 2024, touch interventions","https://www.nature.com/articles/s41562-024-01841-8.pdf","full text"),
          ("Cohen et al. 2015, hugs and colds (Carnegie Mellon)","https://www.cmu.edu/news/stories/archives/2014/december/december17_hugsprotect.html","press release")],
 "nature":[("Meta-analysis of 59 studies, green space and depression/anxiety","https://pmc.ncbi.nlm.nih.gov/articles/PMC10885792","full text")],
 "intimacy":[("Muise et al. 2016, sex frequency (secondary report)","https://www.medicalnewstoday.com/articles/302868","secondary report"),
          ("Cetre et al. 2016, children and wellbeing","https://docs.iza.org/dp9880.pdf","full text"),
          ("Nelson et al. 2012, parenthood and happiness","https://www.psychologicalscience.org/?p=69554","summary"),
          ("Boivin et al. 2011, distress and fertility treatment","https://orca.cardiff.ac.uk/id/eprint/11468/","abstract")],
 "mindfulness":[("Goldberg et al. 2018, mindfulness vs other treatments","https://repository.lsu.edu/psychology_pubs/1041","abstract")],
 "cbt":[("Cuijpers et al. 2023, CBT for depression, 409 trials","https://cris.fau.de/publications/288275935","abstract"),
        ("Cuijpers et al., psychotherapy and publication bias","https://research.vu.nl/en/publications/efficacy-of-cognitive-behavioural-therapy-and-other-psychological/","abstract")],
 "gratitude":[("Gratitude megastudy in 34 countries","https://research.sabanciuniv.edu/id/eprint/54109/","abstract")],
 "kindness":[("Curry et al. 2018, kindness and wellbeing","https://ora.ox.ac.uk/objects/uuid:4701365b-5760-4ece-a390-857a5f7b3c0c","abstract")],
 "music":[("de Witte et al. 2020, music and stress, 104 trials","https://dare.uva.nl/id/41f4d8b7-a651-4ca1-b081-1f06682d6145","abstract")],
 "breathing":[("Fincham et al. 2023, breathwork meta-analysis","https://pmc.ncbi.nlm.nih.gov/articles/PMC9828383/","full text"),
              ("Slow breathing and heart rate variability, 223 studies","https://qastaffprofiles.bournemouth.ac.uk/display/journal-article/368158","abstract")],
 "belonging":[("Holt-Lunstad et al. 2010, social ties and survival","https://doaj.org/article/c9833ba608474b048444b92ae7ee48ad","abstract"),
              ("Hickin et al., psychological loneliness interventions","https://discovery.ucl.ac.uk/id/eprint/10135088/1/CPREV-D-20-00450_R1%20(1).pdf","manuscript"),
              ("Bradbury and Bodenmann 2020, couple therapy","https://pubmed.ncbi.nlm.nih.gov/32031866/","abstract")],
 "meaning":[("Alimujiang et al. 2019, purpose and mortality","https://www.themapofmeaning.org/wp-content/uploads/2025/08/alimujiang_2019_oi_190185.pdf","full text")],
 "stability":[("WHO/ILO 2021, long working hours","https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke-who-ilo","news release"),
              ("Kivimäki et al. 2015, long hours and heart disease, stroke","https://pure.qub.ac.uk/en/publications/long-working-hours-and-risk-of-coronary-heart-disease-and-stroke-/","abstract"),
              ("WHO, burn-out as an occupational phenomenon","https://www.who.int/news-room/detail/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases","WHO")],
 "life":[("Malgaroli et al. 2017, divorce and depression","https://pmc.ncbi.nlm.nih.gov/articles/PMC5637453","full text"),
         ("Bes et al. 2023, burnout interventions","https://link.springer.com/10.1007/s00420-023-02009-z","abstract"),
         ("Lally et al. 2010, how long a habit takes (UCL)","https://www.ucl.ac.uk/news/2009/aug/how-long-does-it-take-form-habit","press release"),
         ("NICE NG116, post-traumatic stress disorder","https://www.nice.org.uk/guidance/ng116/resources/posttraumaticstress-disorder-pdf-66141601777861","guideline"),
         ("Kessler et al. 2017, trauma and PTSD worldwide","https://doaj.org/article/b16a9089153b4957a6264963ba59bea3","abstract"),
         ("US National Academies 2023, social media and adolescent health","https://nap.nationalacademies.org/resource/27396/Highlights_for_Social_Media_and_Adolescent_Health.pdf","report highlights"),
         ("Comtesse et al. 2024, prolonged grief","https://edoc.ku.de/id/eprint/33901/1/1-s2.0-S0165032724001046-main.pdf","full text"),
         ("Mendelian randomisation study, alcohol and depression 2024","https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1372758/full","full text")],
 "background":[("World Happiness Report 2022, biology of happiness","https://www.worldhappiness.report/ed/2022/exploring-the-biological-basis-for-happiness","report"),
         ("Lancet Commission 2024, dementia prevention","https://discovery.ucl.ac.uk/10196488/1/Livingston_Lancet%20Commission%20accepted%20version.pdf","manuscript"),
         ("Childhood maltreatment and depression, 2025 meta-analysis","https://www.nationalelfservice.net/mental-health/depression/can-preventing-childhood-maltreatment-reduce-depression/","summary"),
         ("Perimenopause and depression, 2024 meta-analysis","https://pubmed.ncbi.nlm.nih.gov/38642901/","abstract"),
         ("Leproult and Van Cauter 2011, sleep restriction and testosterone","https://www.sciencedaily.com/releases/2011/05/110531162142.htm","press report")],
}
# which source groups each page uses
NEED_SRC = {"sleep":["sleep"],"movement":["exercise"],"food":["food"],"rhythm-light":["light"],"touch":["touch"],"safe-place":["nature"],"intimacy":["intimacy"],
 "belonging":["belonging"],"meaning":["meaning"],"stability":["stability"],"control":[],"competence":[]}
DOOR_SRC = {"reappraisal":[],"mindfulness":["mindfulness"],"cbt":["cbt"],"gratitude":["gratitude"],"kindness":["kindness"],"exercise":["exercise"],"regular-sleep":["sleep"],
 "morning-light":["light"],"wanted-touch":["touch"],"nature":["nature"],"music":["music"],"breathing":["breathing"]}

SRC["pain"]=[("Cochrane featured review, psychological therapies for chronic pain","https://www.cochrane.org/zh-hans/about-us/news/featured-review-psychological-therapies-management-chronic-pain-excluding-headache-adults","summary"),
 ("NICE NG193 chronic primary pain, as reported by RheumNow","https://rheumnow.com/news/nice-guidelines-chronic-pain-management","secondary report"),
 ("NHS Specialist Pharmacy Service, chronic pain","https://www.medicinesresources.nhs.uk/chronic-pain-primary-and-secondary-in-over-16s-assessment-of-all-chronic-pain-and-management-of-chroni","secondary report"),
 ("Chronic pain and mental disorders, umbrella review (Mental Elf)","https://www.nationalelfservice.net/musculoskeletal/musculoskeletal-pain/chronic-pain-in-mental-disorders-a-widely-overlooked-comorbidity/","summary")]
SRC["illness"]=[("Depression in cancer patients, 70 studies","https://research.regionh.dk/da/publications/prevalence-of-depression-anxiety-and-adjustment-disorder-in-oncol/","abstract"),
 ("Long COVID, depression and anxiety, 165 studies","https://link.springer.com/10.1186/s12888-023-05481-6","abstract"),
 ("COINCIDE trial, collaborative care in diabetes and heart disease","https://eprints.whiterose.ac.uk/106198/1/BMJ_Open_2016_Camacho_.pdf","full text")]
SRC["adhd"]=[("American Psychiatric Association, ADHD in DSM-5","https://www.psychiatry.org/File Library/Psychiatrists/Practice/DSM/APA_DSM-5-ADHD.pdf","fact sheet"),
 ("CDC, ADHD in adults","https://www.cdc.gov/adhd/about/adhd-in-adults.html","public health"),
 ("NIMH, attention-deficit/hyperactivity disorder","https://www.nimh.nih.gov/sites/default/files/documents/health/publications/adhd-2024.pdf","public health"),
 ("NICE NG87, ADHD","https://www.nice.org.uk/guidance/ng87/resources/attention-deficit-hyperactivity-disorder-diagnosis-and-management-pdf-1837699732933","guideline, partly read")]
SRC["autism"]=[("NICE CG142, autism in adults","https://www.nice.org.uk/guidance/cg142/chapter/Key-priorities-for-implementation","guideline"),
 ("Cook et al. 2021, camouflaging in autism","https://research.birmingham.ac.uk/en/publications/camouflaging-in-autism-a-systematic-review/","abstract"),
 ("Hollocks et al. 2019, anxiety and depression in autism","https://ueaeprints.uea.ac.uk/id/eprint/68116/","abstract"),
 ("UCL 2023, number of autistic people in England","https://www.ucl.ac.uk/news/2023/jun/number-autistic-people-england-may-be-twice-high-previously-thought","press release")]
SRC["tech"]=[("Burnell et al. 2025, restricting social media, 32 trials","https://www.rti.org/publication/the-effects-of-social-media-restriction-meta-analytic-evidence-fr","abstract"),
 ("Social media abstinence, 10 studies, 2025","https://pubmed.ncbi.nlm.nih.gov/40038410/","abstract"),
 ("US Surgeon General advisory 2023, social media and youth","https://hhs.gov/sites/default/files/sg-youth-mental-health-social-media-advisory.pdf","advisory")]
SRC["work"]=[("Rönnblad et al. 2019, job insecurity and mental health","https://www.sjweh.fi/article/3797","abstract"),
 ("Bartlett et al. 2019, workplace mindfulness","https://research-portal.uea.ac.uk/en/publications/a-systematic-review-and-meta-analysis-of-workplace-mindfulness-tr/","abstract"),
 ("Shift work and health, umbrella review 2022","https://pubmed.ncbi.nlm.nih.gov/34473048/","abstract"),
 ("Irregular sleep timing and mortality, UK Biobank","https://elifesciences.org/articles/88359","full text")]
SRC["trauma2"]=[("Cochrane, single-session debriefing","https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD000560/pdf/CDSR/CD000560/CD000560_abstract.pdf","abstract")]

SRC["sleeptime"]=[SRC["work"][3]]
