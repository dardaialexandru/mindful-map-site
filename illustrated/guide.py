"""Optional guided reflection (guide.html). Everything runs in the visitor's browser; nothing is sent or stored."""
import json, icons

def data(G, T, NEWCOL):
    from legacy_content import DOORS
    N = G["NEEDS"]; ACC = G["ACC"]; FEEL = G["FEEL"]
    needs = {}
    for k, d in N.items():
        needs[k] = dict(name=d["name"], url=f"need/{k}.html", ev=d["ev"], step=d["tryit"][0], col=ACC[k], kind=d["kind"])
    for t in T:
        if t["dir"] == "need": needs[t["slug"]] = dict(name=t["name"], url=f'need/{t["slug"]}.html', ev=t["ev"], step=t["tryit"][0], col=t["col"], kind="mind")
    OVR = {"stability": "Write down the one worry that weighs most, then one part of it you could change.", "intimacy": "Read the page first. It explains what research does and does not say about closeness."}
    for k, v in OVR.items():
        if k in needs: needs[k]["step"] = v; needs[k]["idea"] = True
    mb = {t["slug"]: t for t in T if t["dir"] == "mindbody"}
    needs["stress"] = dict(name="Stress and the body's defences", url="mindbody/stress.html", ev="partial", step=mb["stress"]["tryit"][0], col=mb["stress"]["col"], kind="mindbody")
    needs["regulation"] = dict(name="How you handle feelings", url="mindbody/regulation.html", ev="partial", step=mb["regulation"]["tryit"][0], col=mb["regulation"]["col"], kind="mindbody")
    feel = {k: dict(name=v["name"], needs=[s[0] for s in v["stops"]]) for k, v in FEEL.items()}
    doors = [dict(slug=d[0], name=d[2], line=d[3], level=d[4], needs=d[-1], step=d[7][0]) for d in DOORS]
    iconsvg = {k: icons.ico(k, needs[k]["col"], 28) for k in needs if k in icons.P or k in icons.ALIAS}
    return dict(needs=needs, feel=feel, doors=doors, icons=iconsvg)

CSS = """<style>
.gd{max-width:720px;margin:0 auto;padding:34px 0 60px}
.gd h1{margin:.2em 0 .3em}
.gd .tag{letter-spacing:.14em;text-transform:uppercase;font-size:.78rem;font-weight:700;color:var(--soft);margin:0}
.gcard{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px 24px;margin:18px 0}
.gbar{height:6px;border-radius:6px;background:var(--line);overflow:hidden;margin:0 0 18px}.gbar i{display:block;height:100%;background:#8A6420;width:0;transition:width .3s}
.gq{font-family:Georgia,'Times New Roman',serif;font-size:1.45rem;line-height:1.3;margin:6px 0 4px}
.gsub{color:var(--soft);font-size:.95rem;margin:0 0 16px}
.gopts{display:grid;gap:10px;margin:14px 0 0}
.gopt{display:flex;align-items:center;gap:12px;text-align:left;width:100%;padding:14px 16px;border:1.5px solid var(--line);border-radius:14px;background:#fff8;font:inherit;font-size:1rem;color:var(--ink);cursor:pointer}
.gopt:hover,.gopt:focus-visible{border-color:#8A6420;outline:none}
.gopt[aria-pressed=true]{border-color:#8A6420;background:#8A64201a;font-weight:700}
.gopt svg{flex:none}
.gscale{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.gscale .gopt{flex-direction:column;justify-content:center;text-align:center;padding:14px 4px;font-size:.82rem;line-height:1.2;min-height:78px}
.gscale .gopt b{font-size:1.25rem}
@media(max-width:520px){.gscale{grid-template-columns:1fr}.gscale .gopt{flex-direction:row;text-align:left;min-height:0;padding:12px 14px;font-size:.95rem}.gscale .gopt b{font-size:1.1rem;width:1.4em}}
.gnav{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:20px}
.gbtn{display:inline-block;padding:12px 22px;border-radius:999px;border:0;background:#8A6420;color:#fff;font:inherit;font-weight:700;cursor:pointer;text-decoration:none}
.gbtn:disabled{opacity:.4;cursor:not-allowed}
.glink{background:none;border:0;font:inherit;color:var(--soft);text-decoration:underline;cursor:pointer;padding:6px 2px}
.gres{display:grid;gap:14px}
.gitem{border:1px solid var(--line);border-left:6px solid var(--c);border-radius:14px;background:var(--card);padding:16px 18px}
.gitem h3{margin:0 0 4px;display:flex;align-items:center;gap:10px;font-size:1.15rem}
.gitem p{margin:.35em 0}
.gstep{margin:10px 0 0;padding:10px 12px;background:#8A64201a;border-radius:10px}
.gcare{border:1.5px solid #8E4A5A;background:#8E4A5A12;border-radius:14px;padding:16px 18px;margin:0 0 16px}
.gnote{font-size:.9rem;color:var(--soft)}
.gstr{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 0}.gstr a{display:inline-flex;align-items:center;gap:8px;padding:7px 14px;border:1.5px solid var(--line);border-radius:999px;text-decoration:none;color:var(--ink);font-weight:600;background:var(--card)}
.gev{display:inline-block;font-size:.82rem;font-weight:700;color:var(--soft)}
</style>"""

JS = r"""
<script>
(function(){
const D = __DATA__;
const OPT3 = [["Most days",2],["Some days",1],["Hardly ever",0]];
const OPT4 = [["Not at all",0],["Several days",1],["More than half the days",2],["Nearly every day",3]];
const FEELS = [["tired","Tired"],["pain","In pain"],["tense","Tense or anxious"],["sad","Sad"],["lonely","Lonely"],["stuck","Stuck"],["pointless","Without purpose"],["calm","Calm"],["good","Good or glad"],["mixed","Not sure"]];
const DUR = [["days","Only a few days"],["weeks","A few weeks"],["months","Several months or longer"]];
/* PHQ-4 (Kroenke, Spitzer, Williams, Loewe): free to use. 0-3 each. Anxiety = items 1+2, low mood = items 3+4. */
const PHQ = [
 {id:"p1",text:"Feeling nervous, anxious or on edge",sub:"anx"},
 {id:"p2",text:"Not being able to stop or control worrying",sub:"anx"},
 {id:"p3",text:"Little interest or pleasure in doing things",sub:"dep"},
 {id:"p4",text:"Feeling down, depressed or hopeless",sub:"dep"}
];
/* Need questions are our own. Score 0-2; rev = the item describes a problem, so the score is flipped. */
const NEEDQ = [
 {id:"sleep",need:"sleep",grp:"body",text:"I slept well enough to feel rested."},
 {id:"movement",need:"movement",grp:"body",text:"My body got to move, and I had some energy."},
 {id:"food",need:"food",grp:"body",text:"I ate regular meals that felt nourishing."},
 {id:"rhythm",need:"rhythm",grp:"body",text:"My days had a regular rhythm, and I got daylight."},
 {id:"touch",need:"touch",grp:"body",text:"I got the physical closeness I wanted, such as a hug or a hand on the shoulder."},
 {id:"safe",need:"safe",grp:"body",text:"I had a place where I could rest and feel safe."},
 {id:"intimacy",need:"intimacy",grp:"body",skip:1,text:"I had the close, romantic or physical connection that I want."},
 {id:"control",need:"control",grp:"mind",text:"I felt I had a say in how my days go."},
 {id:"competence",need:"competence",grp:"mind",text:"I felt able to do things well."},
 {id:"belonging",need:"belonging",grp:"mind",text:"I felt close to people who matter to me."},
 {id:"meaning",need:"meaning",grp:"mind",text:"I felt that what I do matters."},
 {id:"stability",need:"stability",grp:"mind",rev:1,text:"I worried about money, work or where I live."},
 {id:"recognition",need:"recognition",grp:"mind",text:"People noticed and valued my effort."},
 {id:"creativity",need:"creativity",grp:"mind",text:"I made or imagined something, even a small thing: music, writing, crafts, play."},
 {id:"ruminate",need:"regulation",grp:"handle",rev:1,text:"I went over the same worries again and again."},
 {id:"avoid",need:"regulation",grp:"handle",rev:1,text:"When a hard feeling came, I pushed it away or avoided it."},
 {id:"tension",need:"stress",grp:"handle",rev:1,text:"My body felt tight: chest, jaw, stomach, or a racing heart."}
];
const GRPN = {body:"Your body",mind:"Your mind",handle:"How you handle hard moments"};
/* Which needs sit behind which feelings: taken from the feeling pages. Extra context from the PHQ-4 uses the 'close' links on the Connections page. */
const CTX = {dep:{sleep:1,movement:1,meaning:1,belonging:1},anx:{sleep:1,regulation:1,stress:1}};
const EVB = {solid:.5,partial:.25,weak:0};
const LV = {good:3,medium:2,limited:1};
/* Clusters: needs that travel together (see Connections). A pattern is shown when two or more of its needs are often unmet. */
const CLUS = [
 {id:"rest",name:"Rest and rhythm",needs:["sleep","rhythm","movement","food"],text:"Sleep, daylight, movement and food support each other. In studies, exercise improved sleep a little, and regular days and morning light help keep sleep regular.",first:"sleep",links:[["need/sleep.html","Sleep"],["need/rhythm-light.html","Rhythm and light"],["need/movement.html","Movement"]]},
 {id:"people",name:"People and closeness",needs:["belonging","touch","intimacy","recognition"],text:"Closeness, touch and being valued often go together. A few warm relationships mattered more than many distant ones.",first:"belonging",links:[["need/belonging.html","Belonging"],["need/touch.html","Touch"],["feel/lonely.html","Feeling: Lonely"]]},
 {id:"pressure",name:"Pressure and the body",needs:["stability","control","stress","regulation"],text:"Money, work and home worries can start a long stress response, and going over worries keeps it going. Slow breathing is one tested way to settle it.",first:"stress",links:[["mindbody/stress.html","Stress and the body"],["mindbody/breathing.html","Breathing"],["need/stability.html","Stability"]]},
 {id:"purpose",name:"Purpose and ability",needs:["meaning","competence","creativity","control"],text:"Feeling able, having a say and making things go together with a sense that what you do matters.",first:"competence",links:[["need/meaning.html","Meaning"],["need/competence.html","Competence"],["need/creativity.html","Creativity"]]}
];
/* Combinations of answers. Each text comes from a source already on the site. */
const COMBOS = [
 {id:"sleep-anx",when:a=>a.gap.sleep>=1&&a.anx>=3,title:"Poor sleep and anxiety",text:"They feed each other. In a review of 154 experiments, losing sleep raised anxiety and lowered good feelings. Starting with sleep is the best-supported first step.",links:[["need/sleep.html","Sleep"],["door/regular-sleep.html","Regular sleep"],["feel/tense.html","Feeling: Tense or anxious"]]},
 {id:"sleep-move",when:a=>a.gap.sleep>=1&&a.gap.movement>=1,title:"Little sleep and little movement",text:"Exercise improved sleep quality in 9 trials, though the certainty was low. A short walk is a gentle place to start.",links:[["need/movement.html","Movement"],["door/exercise.html","Exercise"]]},
 {id:"dep-move",when:a=>a.dep>=3&&a.gap.movement>=1,title:"Low mood and little movement",text:"In trials, exercise lifted low mood by a moderate amount. Many trials were small, so it is a help and not a cure.",links:[["need/movement.html","Movement"],["feel/sad.html","Feeling: Sad"]]},
 {id:"worry-both",when:a=>a.gap.ruminate>=1&&a.gap.avoid>=1,title:"Going over worries and pushing feelings away",text:"In a review of 114 studies, going over things again and again, and avoiding or pushing down feelings, were among the ways most closely linked with low mood and anxiety. This shows a link, not a cause.",links:[["mindbody/regulation.html","How you handle feelings"],["door/reappraisal.html","Seeing a situation differently"],["door/mindfulness.html","Mindfulness"]]},
 {id:"press-tension",when:a=>a.gap.stability>=1&&a.gap.tension>=1,title:"Money or work worries, and a tense body",text:"Long worries can keep the body's stress response switched on. Slow breathing is one tested way to settle it.",links:[["mindbody/stress.html","Stress and the body"],["mindbody/breathing.html","Breathing"]]},
 {id:"lonely-touch",when:a=>a.gap.belonging>=1&&a.gap.touch>=1,title:"Feeling far from people, and little touch",text:"Wanted touch helped pain, anxiety and mood in the short term in studies, and warm ties mattered most for loneliness.",links:[["need/belonging.html","Belonging"],["need/touch.html","Touch"]]},
 {id:"purpose-stuck",when:a=>a.gap.meaning>=1&&a.gap.competence>=1&&a.gap.control>=1,title:"Purpose, ability and a say, all low",text:"These three often travel together. A small task you can finish is a way back into all three.",links:[["need/control.html","Control"],["need/competence.html","Competence"],["need/meaning.html","Meaning"]]}
];
const S = {feel:[],dur:null,ans:{},seq:[],i:-1,safety:null};
const root = document.getElementById("gd-root");
const $ = (t,a,h)=>{const e=document.createElement(t);if(a)for(const k in a){if(a[k]==null)continue;if(k==="class")e.className=a[k];else if(k.startsWith("on"))e.addEventListener(k.slice(2),a[k]);else e.setAttribute(k,a[k])}if(h!=null)e.innerHTML=h;return e};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function bar(n){return '<div class="gbar" aria-hidden="true"><i style="width:'+Math.round(100*n)+'%"></i></div>'}
function show(node){root.innerHTML="";root.appendChild(node);window.scrollTo({top:root.getBoundingClientRect().top+scrollY-20,behavior:"smooth"});const h=node.querySelector("[data-focus]");if(h)h.focus({preventScroll:true})}
function seq(){return [{t:"feel"},{t:"dur"},{t:"phqintro"}].concat(PHQ.map(q=>({t:"phq",q:q})),[{t:"needintro"}],NEEDQ.map(q=>({t:"need",q:q})),[{t:"safety"}])}
function intro(){
 const c=$("div",{class:"gcard"},'<p class="tag">Optional · about 3 minutes</p><h1 data-focus tabindex="-1">A guided reflection</h1><p>Around 20 short questions about the last two weeks. At the end you get the needs that look most worth your attention, the patterns between them, and one small step for each.</p><p class="gnote">This is not a test and not a diagnosis. Nothing is sent or saved: your answers stay on this page and disappear when you close it. You can skip any question.</p>');
 const nav=$("div",{class:"gnav"});nav.appendChild($("button",{class:"gbtn",onclick:()=>{S.seq=seq();S.i=0;step()}},"Begin"));nav.appendChild($("a",{class:"glink",href:"index.html"},"Back to the map"));c.appendChild(nav);show(c)}
function prog(){return .03+.92*(S.i/(S.seq.length-1))}
function nav(c,skip){const n=$("div",{class:"gnav"});n.appendChild($("button",{class:"glink",onclick:()=>{S.i>0?(S.i--,step()):intro()}},"Back"));if(skip)n.appendChild($("button",{class:"glink",onclick:skip},"Skip this one"));c.appendChild(n)}
function adv(){S.i++;step()}
function step(){
 const s=S.seq[S.i];if(!s)return results();
 if(s.t==="feel")return feel();if(s.t==="dur")return dur();
 if(s.t==="phqintro")return note("Step 1 of 2","How have you been?","Over the last 2 weeks, how often have you been bothered by the following problems?","These four questions are a well-known short screen for low mood and anxiety. They help us see how heavy things feel.");
 if(s.t==="needintro")return note("Step 2 of 2","What your days have held","Now a few questions about your body, your mind and how you handle hard moments. Think about the last two weeks.","There are no right answers. If a question does not fit your life, skip it.");
 if(s.t==="phq")return ask(s.q,OPT4,"phq");if(s.t==="need")return ask(s.q,OPT3,"need");if(s.t==="safety")return safety()}
function note(tag,h,p,g){const c=$("div",{class:"gcard"},bar(prog())+'<p class="tag">'+tag+'</p><p class="gq" data-focus tabindex="-1">'+esc(h)+'</p><p>'+esc(p)+'</p><p class="gnote">'+esc(g)+'</p>');const n=$("div",{class:"gnav"});n.appendChild($("button",{class:"glink",onclick:()=>{S.i--;step()}},"Back"));n.appendChild($("button",{class:"gbtn",onclick:adv},"Continue"));c.appendChild(n);show(c)}
function feel(){
 const c=$("div",{class:"gcard"},bar(prog())+'<p class="gq" data-focus tabindex="-1">How do you feel right now?</p><p class="gsub">Choose up to two. There is no wrong answer.</p>');
 const g=$("div",{class:"gopts"});
 FEELS.forEach(([k,n])=>g.appendChild($("button",{class:"gopt","aria-pressed":S.feel.includes(k)?"true":"false",onclick:()=>{const i=S.feel.indexOf(k);if(i>=0)S.feel.splice(i,1);else{if(k==="mixed")S.feel=[];S.feel=S.feel.filter(x=>x!=="mixed");if(S.feel.length>=2)S.feel.shift();S.feel.push(k)}feel()}},esc(n))));
 c.appendChild(g);const n=$("div",{class:"gnav"});n.appendChild($("button",{class:"glink",onclick:intro},"Back"));n.appendChild($("button",{class:"gbtn",disabled:S.feel.length?null:"disabled",onclick:adv},"Next"));c.appendChild(n);show(c)}
function dur(){
 const c=$("div",{class:"gcard"},bar(prog())+'<p class="gq" data-focus tabindex="-1">How long has it felt like this?</p>');
 const g=$("div",{class:"gopts"});DUR.forEach(([k,n])=>g.appendChild($("button",{class:"gopt","aria-pressed":S.dur===k?"true":"false",onclick:()=>{S.dur=k;adv()}},esc(n))));
 c.appendChild(g);nav(c);show(c)}
function ask(q,opts,kind){
 const lead=kind==="phq"?"Over the last 2 weeks, how often have you been bothered by":"In the last two weeks, how often was this true?";
 const c=$("div",{class:"gcard"},bar(prog())+(q.grp?'<p class="tag">'+GRPN[q.grp]+'</p>':'<p class="tag">Last 2 weeks</p>')+'<p class="gsub">'+lead+'</p><p class="gq" data-focus tabindex="-1">'+esc(q.text)+'</p>');
 const g=$("div",{class:"gopts",role:"group","aria-label":q.text});
 opts.forEach(([n,v])=>g.appendChild($("button",{class:"gopt","aria-pressed":S.ans[q.id]===v?"true":"false",onclick:()=>{S.ans[q.id]=v;adv()}},esc(n))));
 c.appendChild(g);nav(c,()=>{delete S.ans[q.id];adv()});show(c)}
function safety(){
 const c=$("div",{class:"gcard"},bar(.96)+'<p class="gsub">The last question, one we ask everyone</p><p class="gq" data-focus tabindex="-1">Over the last 2 weeks, how often have you had thoughts that you would be better off dead, or of hurting yourself in some way?</p>');
 const g=$("div",{class:"gopts"});OPT4.forEach(([n,v])=>g.appendChild($("button",{class:"gopt",onclick:()=>{S.safety=v;adv()}},esc(n))));g.appendChild($("button",{class:"gopt",onclick:()=>{S.safety=null;adv()}},"I would rather not say"));
 c.appendChild(g);c.appendChild($("p",{class:"gnote"},'If you need to talk to someone now, <a href="help.html">Get help now</a> lists free lines, or call 112.'));nav(c);show(c)}
/* ---- scoring ---- */
function calc(){
 const raw={};NEEDQ.forEach(q=>{const v=S.ans[q.id];if(v==null)return;raw[q.id]=q.rev?2-v:v});
 const gap={};NEEDQ.forEach(q=>{if(raw[q.id]!=null)gap[q.id]=2-raw[q.id]});
 const byNeed={};NEEDQ.forEach(q=>{if(raw[q.id]!=null)(byNeed[q.need]=byNeed[q.need]||[]).push(2-raw[q.id])});
 const ng={};for(const k in byNeed)ng[k]=byNeed[k].reduce((a,b)=>a+b,0)/byNeed[k].length;
 const ph=id=>S.ans[id]==null?0:S.ans[id];
 const anx=ph("p1")+ph("p2"),dep=ph("p3")+ph("p4"),tot=anx+dep;
 const answered=NEEDQ.filter(q=>raw[q.id]!=null).length;
 const unmet=Object.keys(ng).filter(k=>ng[k]>=1).length;
 return {raw,gap,ng,anx,dep,tot,answered,unmet,nNeeds:Object.keys(ng).length}}
function results(){
 const r=calc();const a={gap:r.gap,anx:r.anx,dep:r.dep};
 const linked=new Set();S.feel.forEach(f=>{const i=D.feel[f];if(i)i.needs.forEach(n=>linked.add(n))});
 const cand=Object.keys(r.ng).filter(k=>r.ng[k]>=1&&D.needs[k]).map(k=>{
  let p=r.ng[k]*3+(linked.has(k)?1.5:0)+(EVB[D.needs[k].ev]||0);
  if(r.dep>=3&&CTX.dep[k])p+=1;if(r.anx>=3&&CTX.anx[k])p+=1;return {k,gap:r.ng[k],p}}).sort((x,y)=>y.p-x.p).slice(0,3);
 const strong=Object.keys(r.ng).filter(k=>r.ng[k]===0&&D.needs[k]).sort((x,y)=>(EVB[D.needs[y].ev]||0)-(EVB[D.needs[x].ev]||0)).slice(0,3);
 const out=$("div",{});
 const sf=S.safety;
 if(sf!=null&&sf>0)out.appendChild($("div",{class:"gcare"},'<b>Thank you for answering honestly.</b><p>Those thoughts are more common than people think, and you do not have to carry them alone. If you might act on them, or you are in danger, call <b>112</b> now. <a href="help.html"><b>Free lines by country are on this page.</b></a> A doctor or therapist is a good next step.</p>'));
 if(r.tot>=6||S.dur==="months"){out.appendChild($("div",{class:"gcare"},'<b>It may be worth talking to someone.</b><p>'+(r.tot>=6?'Your answers about the last two weeks suggest that things feel heavy. ':'')+(S.dur==="months"?'It has lasted for months. ':'')+'A doctor or therapist can look at what is going on, whatever the cause. Nothing on this map replaces that. <a href="help.html">Get help now</a>.</p>'))}
 out.appendChild($("div",{class:"gcard"},'<p class="tag">Your reflection</p><h1 data-focus tabindex="-1">What seems most worth your attention</h1><p>'+(r.answered?('You marked <b>'+r.unmet+' of '+r.nNeeds+'</b> areas as often unmet in the last two weeks.'+(r.unmet>=Math.ceil(r.nNeeds*0.6)?' That is a lot at once. Pick one small step, not all of them.':'')):'You skipped most questions, so this is only a light guess.')+(r.tot<6&&(r.anx>=3||r.dep>=3)?' Your answers about '+(r.anx>=3&&r.dep>=3?'worry and low mood':r.anx>=3?'worry and tension':'low mood')+' are at or above the usual mark that screening tools use to suggest a closer look. If it lasts, mention it to a doctor.':'')+'</p><p class="gnote">A starting point, not a diagnosis.</p>'));
 const patterns=[];
 CLUS.forEach(c=>{const hit=c.needs.filter(k=>r.ng[k]>=1);if(hit.length>=2)patterns.push({c:c,hit:hit})});
 COMBOS.forEach(cb=>{if(cb.when(a))patterns.push({cb:cb})});
 const res=$("div",{class:"gres"});
 if(!cand.length&&r.answered)res.appendChild($("div",{class:"gitem",style:"--c:#5E7F5A"},'<h3>Nothing stands out as unmet</h3><p>Your answers do not point to a clear gap. If you still feel off, pick your feeling on the <a href="index.html#start">map</a> and read what research links to it.</p>'));
 cand.forEach((x,ix)=>{const n=D.needs[x.k];
  let doors=D.doors.filter(d=>d.needs.includes(x.k));
  if(x.k==="regulation")doors=D.doors.filter(d=>["reappraisal","mindfulness","breathing"].includes(d.slug));
  if(x.k==="stress")doors=D.doors.filter(d=>["breathing","mindfulness"].includes(d.slug));
  doors.sort((p,q)=>(LV[q.level]||0)-(LV[p.level]||0));doors=doors.slice(0,2);
  const step=doors.length?doors[0].step:n.step;
  const lvl={solid:"Shown to help in studies",partial:"Some evidence, effect small or mixed",weak:"Not enough evidence yet"}[n.ev]||"";
  const why=[];if(x.gap>=1.5)why.push("your answers show it is often missing or under strain");else why.push("your answers show it is only there some of the time");
  if(linked.has(x.k))why.push("it is linked to how you said you feel");if(r.dep>=3&&CTX.dep[x.k])why.push("it is linked to low mood");if(r.anx>=3&&CTX.anx[x.k])why.push("it is linked to worry and tension");
  const it=$("div",{class:"gitem",style:"--c:"+n.col},'<h3>'+(D.icons[x.k]||"")+'<span>'+(ix+1)+'. '+esc(n.name)+'</span></h3><p>Why it is here: '+esc(why.join("; "))+'.</p><p class="gev">'+lvl+'</p><div class="gstep"><b>A small step for this week:</b> '+esc(step)+(!doors.length&&n.idea?'<br><span class="gnote">A reflection, not a tested treatment.</span>':'')+'</div><p style="margin-top:10px"><a href="'+n.url+'"><b>Read about '+esc(n.name)+' →</b></a>'+(doors.length?' · <a href="door/'+doors[0].slug+'.html">Try: '+esc(doors[0].name)+'</a>':'')+'</p>');
  res.appendChild(it)});
 out.appendChild(res);
 if(patterns.length){const g=$("div",{class:"gcard"},'<h2 style="margin:0 0 6px;font-size:1.3rem">Patterns in your answers</h2><p class="gnote">Some of these tend to travel together. They are links found in studies, not proof of cause.</p>');
  patterns.slice(0,4).forEach(p=>{if(p.cb){g.appendChild($("div",{class:"gitem",style:"--c:#B8892B;margin-top:12px"},'<h3>'+esc(p.cb.title)+'</h3><p>'+esc(p.cb.text)+'</p><p>'+p.cb.links.map(l=>'<a href="'+l[0]+'">'+esc(l[1])+'</a>').join(" · ")+'</p>'))}
   else{const nm=p.hit.map(k=>(D.needs[k]||{}).name||k).join(", ");g.appendChild($("div",{class:"gitem",style:"--c:#3F5E7A;margin-top:12px"},'<h3>'+esc(p.c.name)+'</h3><p>Often unmet for you: '+esc(nm)+'.</p><p>'+esc(p.c.text)+'</p><p>'+p.c.links.map(l=>'<a href="'+l[0]+'">'+esc(l[1])+'</a>').join(" · ")+'</p>'))}});
  out.appendChild(g)}
 if(strong.length){const g=$("div",{class:"gcard"},'<h2 style="margin:0 0 6px;font-size:1.3rem">What seems to be working</h2><p class="gnote">Keep these. They are a base to build on.</p>');const w=$("div",{class:"gstr"});strong.forEach(k=>w.appendChild($("a",{href:D.needs[k].url},(D.icons[k]||"")+esc(D.needs[k].name))));g.appendChild(w);out.appendChild(g)}
 out.appendChild($("div",{class:"gcard gnote"},'<p>This reflection is general information from research. It does not replace a doctor or therapist, and it cannot tell you what is wrong. The first four questions are the PHQ-4 (Löwe et al. 2010, <i>Journal of Affective Disorders</i>), a free screening tool, and the last one comes from the same family of questionnaires. The need questions are our own and have not been tested as a scale, so read the result as a prompt for reflection, not a measurement. Your answers were not sent or saved. Closing this page erases them.</p><p><a href="connections.html">See how everything on the map connects →</a></p>'));
 const nv=$("div",{class:"gnav"});nv.appendChild($("button",{class:"gbtn",onclick:()=>{S.feel=[];S.dur=null;S.ans={};S.i=-1;S.safety=null;intro()}},"Start again"));nv.appendChild($("a",{class:"glink",href:"index.html"},"Back to the map"));out.appendChild(nv);
 window.__gresult={cand:cand.map(x=>x.k),patterns:patterns.map(p=>p.cb?p.cb.id:p.c.id),unmet:r.unmet,tot:r.tot,anx:r.anx,dep:r.dep,care:(sf!=null&&sf>0)||r.tot>=6||S.dur==="months"};
 show(out)}
window.__g={S:S,intro:intro,seq:seq,D:D};
intro();
})();
</script>"""

def page(G, T, NEWCOL, header, footer):
    d = data(G, T, NEWCOL)
    js = JS.replace("__DATA__", json.dumps(d, ensure_ascii=False))
    body = header("", "") + CSS + f'<main class="page np" style="--a:#8A6420"><div class="wrap"><div class="gd"><noscript><p>This guided reflection needs JavaScript. You can still use the <a href="index.html">map</a>.</p></noscript><div id="gd-root"></div></div></div></main>' + js + footer("")
    return body
