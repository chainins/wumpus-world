This is an agent could find the gold in a wumpus world.
The basic method is truth-table enumeration-based entailment
(model checking).
In this code, enumerates all possible model by truth-table
and calculate the probability  of alpha is true.
If the probability  is 1, means alpha is True.
If the probability  is 0, means alpha is False.

If the agent finds the wumpus, it would shoot the wumpus.

All of the perceptions could contribute to the KB(Knowledge-Base) at the 
earliest time.

To accelerate this process( reduce both space complexity and time complexity),
this code also takes several measures:
    1) all of the perceptions would append corresponding elements to KB and 
    dicKB (which records the truth-table already determined, and checked in the 
    beginning of the method of model check) AMAP.
    2) symbol list only includes w(i,j) and p(i,j) since breeze and stench are 
    perceptions and would not be influenced by logic calculations.
    3) Only the grids in KB,dicKB and adjacent ones are added to symbol list.

All of the demands are satisfied. The agent could:
    1) find all of the 100% guguaranteed safe grids around current position.
    2) calculate probabilities of the grids around not 100% guaranteed safe.
    3) identify whether a location is safe at the earliest time possible 
    given percepts.
    4) not get killed because of step 2 above, and eventually find gold 
    and win the game if it is reachable.
    
The performance of the code: less than 1 second each round mostly.
    
According to the demands, this code could work well with the original wwsim.py.

In order to observe the result, a modified wwsim.py is also supplied 
though it isn't necessary.
(in the modified wwsim.py, a timer is added in nonGUI, and step counter and "autoRun" 
button are also added in GUI mode)

--------------------------------------------------------------------
wwagent.py was also modified from the original version written by Greg Scott, to do random motions so that this can be the base
of building various kinds of agent that work with the wwsim.py 
wumpus world simulation.

FACING KEY:
  0 = up
  1 = right
  2 = down
  3 = left

Actions
'move' 'grab' 'shoot' 'left' right'


<!--
 /* Font Definitions */
 @font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:variable;
	mso-font-signature:-536869121 1107305727 33554432 0 415 0;}
@font-face
	{font-family:"Arial Unicode MS";
	panose-1:2 11 6 4 2 2 2 2 2 4;
	mso-font-alt:Arial;
	mso-font-charset:0;
	mso-generic-font-family:auto;
	mso-font-pitch:auto;
	mso-font-signature:0 0 0 0 0 0;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-parent:"";
	margin:0in;
	line-height:115%;
	mso-pagination:widow-orphan;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
h1
	{mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:20.0pt;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:1;
	font-size:20.0pt;
	font-family:"Arial",sans-serif;
	mso-font-kerning:0pt;
	mso-ansi-language:EN;
	font-weight:normal;}
h2
	{mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:.25in;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:2;
	font-size:16.0pt;
	font-family:"Arial",sans-serif;
	mso-ansi-language:EN;
	font-weight:normal;}
h3
	{mso-style-noshow:yes;
	mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:16.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:3;
	font-size:14.0pt;
	font-family:"Arial",sans-serif;
	color:#434343;
	mso-ansi-language:EN;
	font-weight:normal;}
h4
	{mso-style-noshow:yes;
	mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:14.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:4;
	font-size:12.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;
	mso-ansi-language:EN;
	font-weight:normal;}
h5
	{mso-style-noshow:yes;
	mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:5;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;
	mso-ansi-language:EN;
	font-weight:normal;}
h6
	{mso-style-noshow:yes;
	mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:6;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;
	mso-ansi-language:EN;
	font-weight:normal;
	font-style:italic;
	mso-bidi-font-style:normal;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
	{mso-style-priority:10;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	font-size:26.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
p.MsoSubtitle, li.MsoSubtitle, div.MsoSubtitle
	{mso-style-priority:11;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-next:Normal;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:16.0pt;
	margin-left:0in;
	line-height:115%;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	font-size:15.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	color:#666666;
	mso-ansi-language:EN;}
span.SpellE
	{mso-style-name:"";
	mso-spl-e:yes;}
span.GramE
	{mso-style-name:"";
	mso-gram-e:yes;}
.MsoChpDefault
	{mso-style-type:export-only;
	mso-default-props:yes;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	mso-ansi-language:EN;}
.MsoPapDefault
	{mso-style-type:export-only;
	line-height:115%;}
 /* Page Definitions */
 @page
	{mso-footnote-separator:url("readme_images/header.htm") fs;
	mso-footnote-continuation-separator:url("readme_images/header.htm") fcs;
	mso-endnote-separator:url("readme_images/header.htm") es;
	mso-endnote-continuation-separator:url("readme_images/header.htm") ecs;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;
	mso-header-margin:.5in;
	mso-footer-margin:.5in;
	mso-page-numbers:1;
	mso-footer:url("readme_images/header.htm") f1;
	mso-paper-source:0;}
div.WordSection1
	{page:WordSection1;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:"Table Normal";
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-priority:99;
	mso-style-parent:"";
	mso-padding-alt:0in 5.4pt 0in 5.4pt;
	mso-para-margin:0in;
	line-height:115%;
	mso-pagination:widow-orphan;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	mso-ansi-language:EN;}
table.a
	{mso-style-name:"";
	mso-tstyle-rowband-size:1;
	mso-tstyle-colband-size:1;
	mso-style-unhide:no;
	mso-padding-alt:5.0pt 5.0pt 5.0pt 5.0pt;
	mso-para-margin:0in;
	line-height:115%;
	mso-pagination:widow-orphan;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	mso-ansi-language:EN;}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext="edit" spidmax="1026"/>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext="edit">
  <o:idmap v:ext="edit" data="1"/>
 </o:shapelayout></xml><![endif]-->
</head>

<body lang=EN-US style='tab-interval:.5in;word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
12.0pt;margin-left:0in'><b style='mso-bidi-font-weight:normal'><span lang=EN
style='font-size:16.0pt;line-height:115%'>Analysis of AI Agent of 
Wumpus Game<o:p></o:p></span></b></p>

<p class=MsoNormal style='margin-top:12.0pt;margin-right:0in;margin-bottom:
12.0pt;margin-left:0in'><span class=GramE><span lang=EN style='font-size:14.0pt;
line-height:115%'></span></span><span lang=EN style='font-size:14.0pt;
line-height:115%'> Chengpi Wu<o:p></o:p></span></p>

<p class=MsoNormal><span lang=EN>Dec 12, 2021</span></p>

<h1><a name="_jj4ury9jccx2"></a><span lang=EN>1.General Introduction</span></h1>

<p class=MsoNormal><span lang=EN>The objective of this code is to find the gold
in a <span class=SpellE>wumpus</span> world by the basic method of truth-table
enumeration-based entailment (model checking).</span></p>

<p class=MsoNormal><span lang=EN>Before the agent moves, it checks all adjacent
grids and enumerates all possible models by truth-table and calculates the
probability of alpha is true where alpha is w(<span class=SpellE><span
class=GramE>i,j</span></span>) and p(<span class=SpellE>i,j</span>) that means
there is a <span class=SpellE>wumpus</span> or a pit.</span></p>

<p class=MsoNormal><span lang=EN>If the probability is 1, means alpha is True <span
class=GramE>( or</span> entailed by KB ).</span></p>

<p class=MsoNormal><span lang=EN>If the probability is 0, means alpha is False <span
class=GramE>( or</span> not alpha entailed by KB ).</span></p>

<p class=MsoNormal><span lang=EN>If the agent finds the <span class=SpellE>wumpus</span>,
it would shoot and kill the <span class=SpellE>wumpus</span> <span class=GramE>(
Figure</span> 1).</span></p>

<p class=MsoNormal><span lang=EN>The results have been verified manually.</span></p>

<p class=MsoNormal><span lang=EN>All of the demands are satisfied. The agent
could:</span></p>

<p class=MsoNormal><span lang=EN>1) find all of the 100% guaranteed safe grids
around the current position.</span></p>

<p class=MsoNormal><span lang=EN>2) calculate probabilities of the grids around
not 100% guaranteed safe.</span></p>

<p class=MsoNormal><span lang=EN>3) identify whether a location is safe at the
earliest time possible given percepts.</span></p>

<p class=MsoNormal><span lang=EN>4) not get killed because of step 2 above, and
eventually find gold and win the game if it is reachable.</span></p>

<p class=MsoNormal><span lang=EN>Figure 1 The rational agent kills <span
class=SpellE>wumpus</span> and grab the gold</span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shapetype
 id="_x0000_t75" coordsize="21600,21600" o:spt="75" o:preferrelative="t"
 path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="image17.png" o:spid="_x0000_i1046" type="#_x0000_t75"
 style='width:271.2pt;height:207.6pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image001.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=277
src="readme_images/image002.gif" v:shapes="image17.png"><![endif]></span></p>

<h1><a name="_540j7lso2ybq"></a><span lang=EN>2. Methods and Added Parts</span></h1>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>To accelerate this <span class=GramE>process(
reduce</span> both space complexity and time complexity), this code takes
several measures:</span></p>

<p class=MsoNormal><span lang=EN>1) all of the perceptions would append
corresponding elements to KB and <span class=SpellE>dicKB</span> (which is a
dictionary records the truth-table already determined, <span class=GramE>like<span
style='mso-spacerun:yes'>  </span>[</span>(w03,True) or (p03,False)], and
checked in the beginning of the method of <span class=SpellE>modelCheck</span>())
AMAP.</span></p>

<p class=MsoNormal><span lang=EN>All of the perceptions could contribute to the
KB (Knowledge-Base) at the earliest time.</span></p>

<p class=MsoNormal><span lang=EN>For example, if the agent is located at (0,3),
and if 'breeze' is in percepts, [“p02”<span class=GramE>,”or</span>”,”p13”]
would be added to KB.</span></p>

<p class=MsoNormal><span lang=EN>2) symbols list only includes w(<span
class=SpellE><span class=GramE>i,j</span></span>) and p(<span class=SpellE>i,j</span>)
since breeze and stench are perceptions and would not be influenced by logic
calculations. </span></p>

<p class=MsoNormal><span lang=EN>3) Only the grids in <span class=SpellE><span
class=GramE>KB,dicKB</span></span> and adjacent ones are added to symbols list.</span></p>

<p class=MsoNormal><span lang=EN>Improved by several measures, the code could
end in less than 1 second in a 4*4 <span class=SpellE>wumpus</span> world in
most <span class=GramE>scenarios(</span>Figure 2).</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure 2 Timer of the code</span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image6.png" o:spid="_x0000_i1045" type="#_x0000_t75" style='width:173.4pt;
 height:2in;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image003.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=231 height=192
src="readme_images/image004.gif" v:shapes="image6.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>To do these works, some new attributes and methods
are added.</span></p>

<h2><a name="_gi5v7kejz7h7"></a><span lang=EN>2.1 Attributes</span></h2>

<p class=MsoNormal><span lang=EN>KB: knowledge base</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>dicKB</span></span><span
lang=EN>: a dictionary of verified truth, like ('w03<span class=GramE>',False</span>),('p03',False)</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>nextfacing</span></span><span
lang=EN>: the goal facing that the agent need to turn</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>nextpos</span></span><span
lang=EN>: the next position that the agent <span class=GramE>want</span> to
move</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>numTrueKB</span></span><span
lang=EN>: counter of True value of KB, used to calculate the probability</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>numTrueAlpha</span></span><span
lang=EN>: counter of True value of KB, used to calculate the probability</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>symbolsList</span></span><span
lang=EN>:<span style='mso-spacerun:yes'>  </span>a list includes all necessary
symbols</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>wumpusGrid</span></span><span
lang=EN>: the position of <span class=SpellE>wumpus</span></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>wumpusAlive</span></span><span
lang=EN>: check whether <span class=SpellE>wumpus</span> died, initial value is
True</span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>visitedGrids</span></span><span
lang=EN>: a list records grids already visited</span></p>

<p class=MsoNormal><span lang=EN>step: counter of steps</span></p>

<h2><a name="_m2snp34vglku"></a><span lang=EN>2.2 Methods Introduction</span></h2>

<p class=MsoNormal><span class=SpellE><span class=GramE><span lang=EN>isTrue</span></span></span><span
class=GramE><span lang=EN>(</span></span><span lang=EN>): </span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>same as the breakout exercise in the class</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span class=GramE><span lang=EN>checkDicKB</span></span></span><span
class=GramE><span lang=EN>(</span></span><span lang=EN>): </span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>check whether the (<span class=SpellE><span
class=GramE>alpha,True</span></span>) or (<span class=SpellE>alpha,False</span>)
already in the dictionary <span class=SpellE>dicKB</span></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>modelCheck</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,symbols</span>,model,KB,alpha,dicKB</span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>emulate the true-value table, check whether alpha is
True when KB is True based on model. Count the number of the True-value of
alpha and KB for the calculation of probabilities later.</span></p>

<p class=MsoNormal><span lang=EN>Recalled by <span class=SpellE>modelCheck</span>
().</span></p>

<p class=MsoNormal><b><span lang=EN>The pseudo code of <span class=GramE>action(</span>)
is below :<o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>If symbols list is empty:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>If <span
class=SpellE><span class=GramE>isTrue</span></span><span class=GramE>(</span><span
class=SpellE>KB,model</span>):<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:2'>                        </span><span
class=SpellE>numTrueKB</span> ++<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:2'>                        </span>if
<span class=SpellE>isTrue</span>(<span class=SpellE><span class=GramE>alpha,mode</span></span>)<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:3'>                                    </span><span
class=SpellE>numTrueAlpha</span>++<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>else:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:2'>                        </span>return
True<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>else:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>p &lt;-
first symbol from symbols list<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>if (<span
class=SpellE><span class=GramE>p,True</span></span>) in <span class=SpellE>self.dicKB</span>:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:2'>                        </span>return
<span class=SpellE>modelCheck</span>(<span class=SpellE><span class=GramE>rest,model</span></span>+[(<span
class=SpellE>p,True</span>)], <span class=SpellE>KB,alpha</span>, <span
class=SpellE>dicKB</span>)<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-spacerun:yes'>            </span><span
class=SpellE>elif</span> (<span class=SpellE><span class=GramE>p,False</span></span>)
in <span class=SpellE>self.dicKB</span>:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-spacerun:yes'>               
</span>return <span class=SpellE>modelCheck</span>(<span class=SpellE><span
class=GramE>rest,model</span></span>+[(<span class=SpellE>p,False</span>)], <span
class=SpellE>KB,alpha</span>, <span class=SpellE>dicKB</span>)<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-spacerun:yes'>            </span>else:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-spacerun:yes'>                </span><span
class=SpellE>firstPart</span> = <span class=SpellE>modelCheck</span>(<span
class=SpellE><span class=GramE>rest,model</span></span>+[(<span class=SpellE>p,True</span>)],<span
class=SpellE>KB,alpha,dicKB</span>) <o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-spacerun:yes'>                </span><span
class=SpellE>secondPart</span> = <span class=SpellE>modelCheck</span>(<span
class=SpellE><span class=GramE>rest,model</span></span>+[(<span class=SpellE>p,False</span>)],<span
class=SpellE>KB,alpha,dicKB</span>)<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-spacerun:yes'>               
</span>return <span class=SpellE>firstPart</span> and <span class=SpellE>secondPart</span><o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>more truth added to <span class=SpellE>dicKB</span>,
more time complexity and space complexity be reduced.</span></p>

<p class=MsoNormal><span lang=EN>Probability of alpha (under <span
class=SpellE><span class=GramE>dicKB,KB</span></span>) = <span class=SpellE>numTrueAlpha</span>
/ <span class=SpellE>numTrueKB</span></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=GramE><span lang=EN>update(</span></span><span
lang=EN>self, percept):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>Original code is modified. </span></p>

<p class=MsoNormal><span lang=EN>According to the latest perceptions, the agent
updates KB &amp; <span class=SpellE>dicKB</span>.</span></p>

<p class=MsoNormal><span lang=EN>(original attribute of map removed in the
code)</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>calculateNextPosition</span></span><span
lang=EN>(self):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>Predict what location it is in based on the direction
it was facing when it <span class=GramE>move</span>.</span></p>

<p class=MsoNormal><span class=GramE><span lang=EN>( maintain</span></span><span
lang=EN> the original code unchanged)</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>calculateNextDirection</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,action</span></span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>the direction the agent is facing needs to be
calculated based on whether the agent turned left/right and what direction it
was facing when it did</span></p>

<p class=MsoNormal><span class=GramE><span lang=EN>( maintain</span></span><span
lang=EN> the original code unchanged)</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>collectGrids</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,complexList</span></span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>collect Grids from (KB) as symbols</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>extractGrids</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,complexList</span></span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>extract Grids from (<span class=SpellE>dicKB</span>)
as symbols</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>symbolCreateList</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,r</span>,c</span>): </span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>create local symbols of adjacent grids and current
grid.</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>calculateProb</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,r</span>,c,alpha</span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>generate probability of alpha by recalling <span
class=SpellE><span class=GramE>modelCheck</span></span><span class=GramE>(</span>).</span></p>

<p class=MsoNormal><span lang=EN>Recalled by <span class=SpellE>trygrid</span>(<span
class=SpellE><span class=GramE>self,r</span>,c</span>).</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>trygrid</span></span><span
lang=EN>(<span class=SpellE><span class=GramE>self,r</span>,c</span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>check whether a grid is <span class=SpellE><span
class=GramE>safe,return</span></span> it to <span class=SpellE>safeList,failList,probList</span>
correspondingly. if it's not sure whether it's safe or a pit or <span
class=SpellE>wumpus</span>, calculates the sum of <span class=GramE>prob(</span><span
class=SpellE>wumpus</span> &amp; pit) by recalling <span class=SpellE>calculateProb</span>().</span></p>

<p class=MsoNormal><span class=GramE><span lang=EN>( the</span></span><span
lang=EN> <span class=SpellE>failList</span> is used to debug and unnecessary at
last )</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>try4grids(<span class=SpellE><span
class=GramE>self,r</span>,c</span>):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>Check whether the 4 adjacent grids are safe.</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span class=SpellE><span lang=EN>calculateAction</span></span><span
lang=EN>(self):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>calculate the turn action according to current and
next facing.</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>action(self):</span></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span lang=EN>Function:
</span></b><span lang=EN>this is the function that will pick the next action of
the agent.</span></p>

<p class=MsoNormal><b><span lang=EN>The pseudo code of <span class=GramE>action(</span>)
is below :<o:p></o:p></span></b></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>step+=1<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>If the last action is turn direction and reaches goal
facing:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>If face
the <span class=SpellE>wumpus</span><o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in;text-indent:.5in'><i
style='mso-bidi-font-style:normal'><span lang=EN style='color:#0B5394'>shoot <o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>If face a goal position<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in;text-indent:.5in'><i
style='mso-bidi-font-style:normal'><span lang=EN style='color:#0B5394'>move<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>Return<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
mso-bidi-font-family:"Arial Unicode MS";color:#0B5394'>else</span></i><i
style='mso-bidi-font-style:normal'><span lang=ZH-CN style='font-family:"Arial Unicode MS";
mso-fareast-font-family:"Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS";
color:#0B5394'>：</span><span lang=EN style='color:#0B5394'><o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Turn
direction continuously<o:p></o:p></span></i></p>

<p class=MsoNormal style='text-indent:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>Return<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>If the agent won:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Action =
Exit<o:p></o:p></span></i></p>

<p class=MsoNormal style='text-indent:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>return<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><span class=GramE><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>If<span style='mso-spacerun:yes'>  </span>the</span></i></span><i
style='mso-bidi-font-style:normal'><span lang=EN style='color:#0B5394'> agent
percept glitter:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Action =
Grab<o:p></o:p></span></i></p>

<p class=MsoNormal style='text-indent:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>return<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>If a grid in possible safe grids list and belong to
visited grids list:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Move to
safe grids list<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>If find <span class=SpellE>wumpus</span>:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>If face
it: <o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Action
= ‘shoot’<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>Else:<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Action
= turn direction<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>Search unvisited grid in safe grid list and select
randomly:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>If all
grids have been visited:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:2'>                        </span>Jump
out to possible safe grids list with a probability <span class=GramE>( default</span>
value is 20%)<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Else:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:2'>                        </span>Choose
one unvisited safe grid randomly<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>If safe grids list is null or jumped out of it with a
probability:<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Sort
possible safe grids list by probabilities<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><span style='mso-tab-count:1'>            </span>if there
are more than 1 grid has the least <span class=GramE>value(</span>least risky):
<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in;text-indent:.5in'><i
style='mso-bidi-font-style:normal'><span lang=EN style='color:#0B5394'>Choose
one grid randomly<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'>Else:<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-left:.5in'><i style='mso-bidi-font-style:normal'><span
lang=EN style='color:#0B5394'><span style='mso-tab-count:1'>            </span>Choose
it<o:p></o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'><o:p>&nbsp;</o:p></span></i></p>

<p class=MsoNormal><i style='mso-bidi-font-style:normal'><span lang=EN
style='color:#0B5394'>Return action<o:p></o:p></span></i></p>

<h1><a name="_h4s9neo32wbq"></a><span lang=EN>3. Results</span></h1>

<p class=MsoNormal><span lang=EN>To compare the two agents of rational agent
(marked as “smart” in the <span class=GramE>code)<span
style='mso-spacerun:yes'>  </span>and</span> random agent, 10 groups are
established. The results show that in most scenarios the rational agent is much
better (Table 1). In the 10 groups, the rational agent grabs gold for 7 times,
falls in pits for 3 times, the random agent is eaten by <span class=SpellE>wumpus</span>
for 1 time, grabs gold for 1 time, and falls in pits for 8 times.</span></p>

<p class=MsoNormal><span lang=EN>However, in some scenarios both agents fail
(group 3,8,9). Because the rational agent could go more steps, which means the
performance score is smaller (Absolute value of the negative number is bigger) <span
class=GramE>( group</span> 3,8 ). That’s inevitable. </span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Table <span class=GramE>1<span
style='mso-spacerun:yes'>  </span>The</span> results of 10 contrast groups</span></p>

<table class=a border=1 cellspacing=0 cellpadding=0 width=623 style='border-collapse:
 collapse;mso-table-layout-alt:fixed;border:none;mso-border-alt:solid black 1.0pt;
 mso-yfti-tbllook:1536;mso-padding-alt:5.0pt 5.0pt 5.0pt 5.0pt;mso-border-insideh:
 1.0pt solid black;mso-border-insidev:1.0pt solid black'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Group</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Agent </span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Result</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Steps Before End</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>1</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>32</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 2</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Wumpus ate</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>3</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>2</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>43</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 3</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>2</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>3</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>843</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 4</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>53</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:7'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>4</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>186</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 5</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:8'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>21</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:9'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>5</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>86</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 6</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:10'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>2</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:11'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>6</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>15</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 7</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:12'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>6</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:13'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>7</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>18</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 8</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:14'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>21</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:15'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>8</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>176</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 9</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:16'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>2</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:17'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>9</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>3</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 10</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:18'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Fell in pit</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>16</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:19'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>10</span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN style='font-family:"Arial Unicode MS";mso-fareast-font-family:"Arial Unicode MS";
  mso-bidi-font-family:"Arial Unicode MS"'>Rational Agent (Smart</span><span
  lang=ZH-CN style='font-family:"Arial Unicode MS";mso-fareast-font-family:
  "Arial Unicode MS";mso-bidi-font-family:"Arial Unicode MS"'>）</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>31</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Figure 11</span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:20;mso-yfti-lastrow:yes'>
  <td width=62 valign=top style='width:46.5pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black 1.0pt;padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=179 valign=top style='width:134.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Random Agent</span></p>
  </td>
  <td width=123 valign=top style='width:92.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>Grab gold</span></p>
  </td>
  <td width=155 valign=top style='width:116.25pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN>43</span></p>
  </td>
  <td width=104 valign=top style='width:78.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black 1.0pt;mso-border-left-alt:solid black 1.0pt;
  padding:5.0pt 5.0pt 5.0pt 5.0pt'>
  <p class=MsoNormal style='line-height:normal;mso-pagination:none'><span
  lang=EN><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure <span class=GramE>2<span
style='mso-spacerun:yes'>  </span>Result</span> of contrast group 1</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image22.png" o:spid="_x0000_i1044" type="#_x0000_t75" style='width:346.8pt;
 height:258pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image005.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=462 height=344
src="readme_images/image006.gif" v:shapes="image22.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image14.png" o:spid="_x0000_i1043" type="#_x0000_t75" style='width:351pt;
 height:258pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image007.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=468 height=344
src="readme_images/image008.gif" v:shapes="image14.png"><![endif]></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure 3 Result of contrast group 2</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image10.png" o:spid="_x0000_i1042" type="#_x0000_t75" style='width:348pt;
 height:258.6pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image009.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=464 height=345
src="readme_images/image010.gif" v:shapes="image10.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image19.png" o:spid="_x0000_i1041" type="#_x0000_t75" style='width:349.2pt;
 height:264pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image011.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=466 height=352
src="readme_images/image012.gif" v:shapes="image19.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure <span class=GramE>4<span
style='mso-spacerun:yes'>  </span>Result</span> of contrast group 3</span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image13.png" o:spid="_x0000_i1040" type="#_x0000_t75" style='width:340.8pt;
 height:250.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image013.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=454 height=334
src="readme_images/image014.gif" v:shapes="image13.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image8.png" o:spid="_x0000_i1039" type="#_x0000_t75" style='width:347.4pt;
 height:258.6pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image015.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=463 height=345
src="readme_images/image016.gif" v:shapes="image8.png"><![endif]></span><span
lang=EN><br clear=all style='mso-special-character:line-break;page-break-before:
always'>
</span></p>

<p class=MsoNormal><span lang=EN>Figure <span class=GramE>5<span
style='mso-spacerun:yes'>  </span>Result</span> of contrast group 4</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image5.png" o:spid="_x0000_i1038" type="#_x0000_t75" style='width:346.2pt;
 height:258pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image017.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=462 height=344
src="readme_images/image018.gif" v:shapes="image5.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image3.png" o:spid="_x0000_i1037" type="#_x0000_t75" style='width:348.6pt;
 height:260.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image019.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=465 height=347
src="readme_images/image020.gif" v:shapes="image3.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure 6 Result of contrast group 5</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image21.png" o:spid="_x0000_i1036" type="#_x0000_t75" style='width:348.6pt;
 height:256.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image021.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=465 height=342
src="readme_images/image022.gif" v:shapes="image21.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image11.png" o:spid="_x0000_i1035" type="#_x0000_t75" style='width:351pt;
 height:258.6pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image023.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=468 height=345
src="readme_images/image024.gif" v:shapes="image11.png"><![endif]></span><span
lang=EN><br clear=all style='mso-special-character:line-break;page-break-before:
always'>
</span><span lang=EN style='font-size:16.0pt;line-height:115%'><o:p></o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure 7 Result of contrast group 6</span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image7.png" o:spid="_x0000_i1034" type="#_x0000_t75" style='width:351.6pt;
 height:257.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image025.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=469 height=343
src="readme_images/image026.gif" v:shapes="image7.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image2.png" o:spid="_x0000_i1033" type="#_x0000_t75" style='width:348pt;
 height:260.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image027.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=464 height=347
src="readme_images/image028.gif" v:shapes="image2.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure 8 Result of contrast group 7</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image12.png" o:spid="_x0000_i1032" type="#_x0000_t75" style='width:355.2pt;
 height:263.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image029.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=474 height=351
src="readme_images/image030.gif" v:shapes="image12.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image4.png" o:spid="_x0000_i1031" type="#_x0000_t75" style='width:356.4pt;
 height:264.6pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image031.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=475 height=353
src="readme_images/image032.gif" v:shapes="image4.png"><![endif]></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure <span class=GramE>9<span
style='mso-spacerun:yes'>  </span>Result</span> of contrast group 8</span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image16.png" o:spid="_x0000_i1030" type="#_x0000_t75" style='width:364.2pt;
 height:264pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image033.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=486 height=352
src="readme_images/image034.gif" v:shapes="image16.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image18.png" o:spid="_x0000_i1029" type="#_x0000_t75" style='width:357pt;
 height:263.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image035.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=476 height=351
src="readme_images/image036.gif" v:shapes="image18.png"><![endif]></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure <span class=GramE>10<span
style='mso-spacerun:yes'>  </span>Result</span> of contrast group 9</span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image15.png" o:spid="_x0000_i1028" type="#_x0000_t75" style='width:355.8pt;
 height:266.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image037.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=474 height=355
src="readme_images/image038.gif" v:shapes="image15.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image1.png" o:spid="_x0000_i1027" type="#_x0000_t75" style='width:351.6pt;
 height:257.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image039.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=469 height=343
src="readme_images/image040.gif" v:shapes="image1.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<span lang=EN style='font-size:11.0pt;line-height:115%;font-family:"Arial",sans-serif;
mso-fareast-font-family:Arial;mso-ansi-language:EN;mso-fareast-language:ZH-CN;
mso-bidi-language:AR-SA'><br clear=all style='mso-special-character:line-break;
page-break-before:always'>
</span>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN>Figure <span class=GramE>11<span
style='mso-spacerun:yes'>  </span>Result</span> of contrast group 10</span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image20.png" o:spid="_x0000_i1026" type="#_x0000_t75" style='width:354pt;
 height:263.4pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image041.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=472 height=351
src="readme_images/image042.gif" v:shapes="image20.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN style='mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="image9.png" o:spid="_x0000_i1025" type="#_x0000_t75" style='width:357pt;
 height:262.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="readme_images/image043.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=476 height=350
src="readme_images/image044.gif" v:shapes="image9.png"><![endif]></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<h1><a name="_btmjji5030if"></a><span lang=EN>4. Extra Work</span></h1>

<p class=MsoNormal><span lang=EN><span style='mso-spacerun:yes'>    </span></span></p>

<p class=MsoNormal><span lang=EN><b style='mso-bidi-font-weight:
normal'><span style='color:red'>This code could work well with the original
wwsim.py unchanged</span></b>.</span></p>

<p class=MsoNormal><span lang=EN>However, it’s very difficult to compare the
two agents in the same scenarios with the original wwsim.py.</span></p>

<p class=MsoNormal><span lang=EN>In order to observe, debug and compare the two
agents in the same scenarios, a modified wwsim.py is also supplied though it
isn't necessary and demanded<span style='color:red'>. <b style='mso-bidi-font-weight:
normal'>It could be ignored if the wwsim.py is demanded unchanged</b></span><b
style='mso-bidi-font-weight:normal'>.<o:p></o:p></b></span></p>

<p class=MsoNormal><span lang=EN>In the <span class=SpellE>nonGUI</span> mode
of the modified wwsim.py, a timer is added. In the GUI mode, a steps counter
and two buttons <span class=GramE>of<span style='mso-spacerun:yes'>  </span>“</span>Rd/<span
class=SpellE>Smt</span>” (switch between random and rational(smart) agents) and
&quot;<span class=SpellE>autoRun</span>&quot; (move 500 steps
automatically)<span style='mso-spacerun:yes'>  </span>are added. Running the
new wwsim.py and the new wwagent.py makes the comparison very easy.</span></p>

<p class=MsoNormal><span lang=EN>If the “<span class=SpellE>autoRun</span>”
button is clicked, the agent would go at most 500 steps <span class=GramE>( 500</span>
is a default value, of course it could be reset in the code). The game ends
before 500 steps if the agent wins or fails in advance. If the game doesn’t end
after 500 steps, the button could be clicked again and try another 500 steps
continuously. </span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><span lang=EN><o:p>&nbsp;</o:p></span></p>

</div>



