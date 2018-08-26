import requests 
from lxml import html


html_list = """<div class="slides" style="width: 1608px;"><div style="position: absolute; left: 1px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">January</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td><a href="?d=0101">1</a></td>
<td><a href="?d=0102">2</a></td>
<td><a href="?d=0103">3</a></td>
<td><a href="?d=0104">4</a></td>
<td><a href="?d=0105">5</a></td>
<td><a href="?d=0106">6</a></td>
<td><a href="?d=0107">7</a></td>
</tr>
<tr align="center"><td><a href="?d=0108">8</a></td>
<td><a href="?d=0109">9</a></td>
<td><a href="?d=0110">10</a></td>
<td><a href="?d=0111">11</a></td>
<td><a href="?d=0112">12</a></td>
<td><a href="?d=0113">13</a></td>
<td><a href="?d=0114">14</a></td>
</tr>
<tr align="center"><td><a href="?d=0115">15</a></td>
<td><a href="?d=0116">16</a></td>
<td><a href="?d=0117">17</a></td>
<td><a href="?d=0118">18</a></td>
<td><a href="?d=0119">19</a></td>
<td><a href="?d=0120">20</a></td>
<td><a href="?d=0121">21</a></td>
</tr>
<tr align="center"><td><a href="?d=0122">22</a></td>
<td><a href="?d=0123">23</a></td>
<td><a href="?d=0124">24</a></td>
<td><a href="?d=0125">25</a></td>
<td><a href="?d=0126">26</a></td>
<td><a href="?d=0127">27</a></td>
<td><a href="?d=0128">28</a></td>
</tr>
<tr align="center"><td><a href="?d=0129">29</a></td>
<td><a href="?d=0130">30</a></td>
<td><a href="?d=0131">31</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 135px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">February</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0201">1</a></td>
<td><a href="?d=0202">2</a></td>
<td><a href="?d=0203">3</a></td>
<td><a href="?d=0204">4</a></td>
</tr>
<tr align="center"><td><a href="?d=0205">5</a></td>
<td><a href="?d=0206">6</a></td>
<td><a href="?d=0207">7</a></td>
<td><a href="?d=0208">8</a></td>
<td><a href="?d=0209">9</a></td>
<td><a href="?d=0210">10</a></td>
<td><a href="?d=0211">11</a></td>
</tr>
<tr align="center"><td><a href="?d=0212">12</a></td>
<td><a href="?d=0213">13</a></td>
<td><a href="?d=0214">14</a></td>
<td><a href="?d=0215">15</a></td>
<td><a href="?d=0216">16</a></td>
<td><a href="?d=0217">17</a></td>
<td><a href="?d=0218">18</a></td>
</tr>
<tr align="center"><td><a href="?d=0219">19</a></td>
<td><a href="?d=0220">20</a></td>
<td><a href="?d=0221">21</a></td>
<td><a href="?d=0222">22</a></td>
<td><a href="?d=0223">23</a></td>
<td><a href="?d=0224">24</a></td>
<td><a href="?d=0225">25</a></td>
</tr>
<tr align="center"><td><a href="?d=0226">26</a></td>
<td><a href="?d=0227">27</a></td>
<td><a href="?d=0228">28</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 269px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">March</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0301">1</a></td>
<td><a href="?d=0302">2</a></td>
<td><a href="?d=0303">3</a></td>
<td><a href="?d=0304">4</a></td>
</tr>
<tr align="center"><td><a href="?d=0305">5</a></td>
<td><a href="?d=0306">6</a></td>
<td><a href="?d=0307">7</a></td>
<td><a href="?d=0308">8</a></td>
<td><a href="?d=0309">9</a></td>
<td><a href="?d=0310">10</a></td>
<td><a href="?d=0311">11</a></td>
</tr>
<tr align="center"><td><a href="?d=0312">12</a></td>
<td><a href="?d=0313">13</a></td>
<td><a href="?d=0314">14</a></td>
<td><a href="?d=0315">15</a></td>
<td><a href="?d=0316">16</a></td>
<td><a href="?d=0317">17</a></td>
<td><a href="?d=0318">18</a></td>
</tr>
<tr align="center"><td><a href="?d=0319">19</a></td>
<td><a href="?d=0320">20</a></td>
<td><a href="?d=0321">21</a></td>
<td><a href="?d=0322">22</a></td>
<td><a href="?d=0323">23</a></td>
<td><a href="?d=0324">24</a></td>
<td><a href="?d=0325">25</a></td>
</tr>
<tr align="center"><td><a href="?d=0326">26</a></td>
<td><a href="?d=0327">27</a></td>
<td><a href="?d=0328">28</a></td>
<td><a href="?d=0329">29</a></td>
<td><a href="?d=0330">30</a></td>
<td><a href="?d=0331">31</a></td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 403px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">April</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0401">1</a></td>
</tr>
<tr align="center"><td><a href="?d=0402">2</a></td>
<td><a href="?d=0403">3</a></td>
<td><a href="?d=0404">4</a></td>
<td><a href="?d=0405">5</a></td>
<td><a href="?d=0406">6</a></td>
<td><a href="?d=0407">7</a></td>
<td><a href="?d=0408">8</a></td>
</tr>
<tr align="center"><td><a href="?d=0409">9</a></td>
<td><a href="?d=0410">10</a></td>
<td><a href="?d=0411">11</a></td>
<td><a href="?d=0412">12</a></td>
<td><a href="?d=0413">13</a></td>
<td><a href="?d=0414">14</a></td>
<td><a href="?d=0415">15</a></td>
</tr>
<tr align="center"><td><a href="?d=0416">16</a></td>
<td><a href="?d=0417">17</a></td>
<td><a href="?d=0418">18</a></td>
<td><a href="?d=0419">19</a></td>
<td><a href="?d=0420">20</a></td>
<td><a href="?d=0421">21</a></td>
<td><a href="?d=0422">22</a></td>
</tr>
<tr align="center"><td><a href="?d=0423">23</a></td>
<td><a href="?d=0424">24</a></td>
<td><a href="?d=0425">25</a></td>
<td><a href="?d=0426">26</a></td>
<td><a href="?d=0427">27</a></td>
<td><a href="?d=0428">28</a></td>
<td><a href="?d=0429">29</a></td>
</tr>
<tr align="center"><td><a href="?d=0430">30</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 537px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">May</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td><a href="?d=0501">1</a></td>
<td><a href="?d=0502">2</a></td>
<td><a href="?d=0503">3</a></td>
<td><a href="?d=0504">4</a></td>
<td><a href="?d=0505">5</a></td>
<td><a href="?d=0506">6</a></td>
</tr>
<tr align="center"><td><a href="?d=0507">7</a></td>
<td><a href="?d=0508">8</a></td>
<td><a href="?d=0509">9</a></td>
<td><a href="?d=0510">10</a></td>
<td><a href="?d=0511">11</a></td>
<td><a href="?d=0512">12</a></td>
<td><a href="?d=0513">13</a></td>
</tr>
<tr align="center"><td><a href="?d=0514">14</a></td>
<td><a href="?d=0515">15</a></td>
<td><a href="?d=0516">16</a></td>
<td><a href="?d=0517">17</a></td>
<td><a href="?d=0518">18</a></td>
<td><a href="?d=0519">19</a></td>
<td><a href="?d=0520">20</a></td>
</tr>
<tr align="center"><td><a href="?d=0521">21</a></td>
<td><a href="?d=0522">22</a></td>
<td><a href="?d=0523">23</a></td>
<td><a href="?d=0524">24</a></td>
<td><a href="?d=0525">25</a></td>
<td><a href="?d=0526">26</a></td>
<td><a href="?d=0527">27</a></td>
</tr>
<tr align="center"><td><a href="?d=0528">28</a></td>
<td><a href="?d=0529">29</a></td>
<td><a href="?d=0530">30</a></td>
<td><a href="?d=0531">31</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 671px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">June</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0601">1</a></td>
<td><a href="?d=0602">2</a></td>
<td><a href="?d=0603">3</a></td>
</tr>
<tr align="center"><td><a href="?d=0604">4</a></td>
<td><a href="?d=0605">5</a></td>
<td><a href="?d=0606">6</a></td>
<td><a href="?d=0607">7</a></td>
<td><a href="?d=0608">8</a></td>
<td><a href="?d=0609">9</a></td>
<td><a href="?d=0610">10</a></td>
</tr>
<tr align="center"><td><a href="?d=0611">11</a></td>
<td><a href="?d=0612">12</a></td>
<td><a href="?d=0613">13</a></td>
<td><a href="?d=0614">14</a></td>
<td><a href="?d=0615">15</a></td>
<td><a href="?d=0616">16</a></td>
<td><a href="?d=0617">17</a></td>
</tr>
<tr align="center"><td><a href="?d=0618">18</a></td>
<td><a href="?d=0619">19</a></td>
<td><a href="?d=0620">20</a></td>
<td><a href="?d=0621">21</a></td>
<td><a href="?d=0622">22</a></td>
<td><a href="?d=0623">23</a></td>
<td><a href="?d=0624">24</a></td>
</tr>
<tr align="center"><td><a href="?d=0625">25</a></td>
<td><a href="?d=0626">26</a></td>
<td><a href="?d=0627">27</a></td>
<td><a href="?d=0628">28</a></td>
<td><a href="?d=0629">29</a></td>
<td><a href="?d=0630">30</a></td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 805px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">July</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0701">1</a></td>
</tr>
<tr align="center"><td><a href="?d=0702">2</a></td>
<td><a href="?d=0703">3</a></td>
<td><a href="?d=0704">4</a></td>
<td><a href="?d=0705">5</a></td>
<td><a href="?d=0706">6</a></td>
<td><a href="?d=0707">7</a></td>
<td><a href="?d=0708">8</a></td>
</tr>
<tr align="center"><td><a href="?d=0709">9</a></td>
<td><a href="?d=0710">10</a></td>
<td><a href="?d=0711">11</a></td>
<td><a href="?d=0712">12</a></td>
<td><a href="?d=0713">13</a></td>
<td><a href="?d=0714">14</a></td>
<td><a href="?d=0715">15</a></td>
</tr>
<tr align="center"><td><a href="?d=0716">16</a></td>
<td><a href="?d=0717">17</a></td>
<td><a href="?d=0718">18</a></td>
<td><a href="?d=0719">19</a></td>
<td><a href="?d=0720">20</a></td>
<td><a href="?d=0721">21</a></td>
<td><a href="?d=0722">22</a></td>
</tr>
<tr align="center"><td><a href="?d=0723">23</a></td>
<td><a href="?d=0724">24</a></td>
<td><a href="?d=0725">25</a></td>
<td><a href="?d=0726">26</a></td>
<td><a href="?d=0727">27</a></td>
<td><a href="?d=0728">28</a></td>
<td><a href="?d=0729">29</a></td>
</tr>
<tr align="center"><td><a href="?d=0730">30</a></td>
<td><a href="?d=0731">31</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 939px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">August</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0801">1</a></td>
<td><a href="?d=0802">2</a></td>
<td><a href="?d=0803">3</a></td>
<td><a href="?d=0804">4</a></td>
<td><a href="?d=0805">5</a></td>
</tr>
<tr align="center"><td><a href="?d=0806">6</a></td>
<td><a href="?d=0807">7</a></td>
<td><a href="?d=0808">8</a></td>
<td><a href="?d=0809">9</a></td>
<td><a href="?d=0810">10</a></td>
<td><a href="?d=0811">11</a></td>
<td><a href="?d=0812">12</a></td>
</tr>
<tr align="center"><td><a href="?d=0813">13</a></td>
<td><a href="?d=0814">14</a></td>
<td><a href="?d=0815">15</a></td>
<td><a href="?d=0816">16</a></td>
<td><a href="?d=0817">17</a></td>
<td><a href="?d=0818">18</a></td>
<td><a href="?d=0819">19</a></td>
</tr>
<tr align="center"><td><a href="?d=0820">20</a></td>
<td><a href="?d=0821">21</a></td>
<td><a href="?d=0822">22</a></td>
<td><a href="?d=0823">23</a></td>
<td><a href="?d=0824">24</a></td>
<td><a href="?d=0825">25</a></td>
<td><a href="?d=0826">26</a></td>
</tr>
<tr align="center"><td><a href="?d=0827">27</a></td>
<td><a href="?d=0828">28</a></td>
<td><a href="?d=0829">29</a></td>
<td><a href="?d=0830">30</a></td>
<td><a href="?d=0831">31</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 1073px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">September</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=0901">1</a></td>
<td><a href="?d=0902">2</a></td>
</tr>
<tr align="center"><td><a href="?d=0903">3</a></td>
<td><a href="?d=0904">4</a></td>
<td><a href="?d=0905">5</a></td>
<td><a href="?d=0906">6</a></td>
<td><a href="?d=0907">7</a></td>
<td><a href="?d=0908">8</a></td>
<td><a href="?d=0909">9</a></td>
</tr>
<tr align="center"><td><a href="?d=0910">10</a></td>
<td><a href="?d=0911">11</a></td>
<td><a href="?d=0912">12</a></td>
<td><a href="?d=0913">13</a></td>
<td><a href="?d=0914">14</a></td>
<td><a href="?d=0915">15</a></td>
<td><a href="?d=0916">16</a></td>
</tr>
<tr align="center"><td><a href="?d=0917">17</a></td>
<td><a href="?d=0918">18</a></td>
<td><a href="?d=0919">19</a></td>
<td><a href="?d=0920">20</a></td>
<td><a href="?d=0921">21</a></td>
<td><a href="?d=0922">22</a></td>
<td><a href="?d=0923">23</a></td>
</tr>
<tr align="center"><td><a href="?d=0924">24</a></td>
<td><a href="?d=0925">25</a></td>
<td><a href="?d=0926">26</a></td>
<td><a href="?d=0927">27</a></td>
<td><a href="?d=0928">28</a></td>
<td><a href="?d=0929">29</a></td>
<td><a href="?d=0930">30</a></td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: 1207px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">October</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td><a href="?d=1001">1</a></td>
<td><a href="?d=1002">2</a></td>
<td><a href="?d=1003">3</a></td>
<td><a href="?d=1004">4</a></td>
<td><a href="?d=1005">5</a></td>
<td><a href="?d=1006">6</a></td>
<td><a href="?d=1007">7</a></td>
</tr>
<tr align="center"><td><a href="?d=1008">8</a></td>
<td><a href="?d=1009">9</a></td>
<td><a href="?d=1010">10</a></td>
<td><a href="?d=1011">11</a></td>
<td><a href="?d=1012">12</a></td>
<td><a href="?d=1013">13</a></td>
<td><a href="?d=1014">14</a></td>
</tr>
<tr align="center"><td><a href="?d=1015">15</a></td>
<td><a href="?d=1016">16</a></td>
<td><a href="?d=1017">17</a></td>
<td><a href="?d=1018">18</a></td>
<td><a href="?d=1019">19</a></td>
<td><a href="?d=1020">20</a></td>
<td><a href="?d=1021">21</a></td>
</tr>
<tr align="center"><td><a href="?d=1022">22</a></td>
<td><a href="?d=1023">23</a></td>
<td><a href="?d=1024">24</a></td>
<td><a href="?d=1025">25</a></td>
<td><a href="?d=1026">26</a></td>
<td><a href="?d=1027">27</a></td>
<td><a href="?d=1028">28</a></td>
</tr>
<tr align="center"><td><a href="?d=1029">29</a></td>
<td><a href="?d=1030">30</a></td>
<td><a href="?d=1031">31</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: -267px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">November</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=1101">1</a></td>
<td><a href="?d=1102">2</a></td>
<td><a href="?d=1103">3</a></td>
<td><a href="?d=1104">4</a></td>
</tr>
<tr align="center"><td><a href="?d=1105">5</a></td>
<td><a href="?d=1106">6</a></td>
<td><a href="?d=1107">7</a></td>
<td><a href="?d=1108">8</a></td>
<td><a href="?d=1109">9</a></td>
<td><a href="?d=1110">10</a></td>
<td><a href="?d=1111">11</a></td>
</tr>
<tr align="center"><td><a href="?d=1112">12</a></td>
<td><a href="?d=1113">13</a></td>
<td><a href="?d=1114">14</a></td>
<td><a href="?d=1115">15</a></td>
<td><a href="?d=1116">16</a></td>
<td><a href="?d=1117">17</a></td>
<td><a href="?d=1118">18</a></td>
</tr>
<tr align="center"><td><a href="?d=1119">19</a></td>
<td><a href="?d=1120">20</a></td>
<td><a href="?d=1121">21</a></td>
<td><a href="?d=1122">22</a></td>
<td><a href="?d=1123">23</a></td>
<td><a href="?d=1124">24</a></td>
<td><a href="?d=1125">25</a></td>
</tr>
<tr align="center"><td><a href="?d=1126">26</a></td>
<td><a href="?d=1127">27</a></td>
<td><a href="?d=1128">28</a></td>
<td><a href="?d=1129">29</a></td>
<td><a href="?d=1130">30</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
<div style="position: absolute; left: -133px; display: block;"><table width="100%" style="border: 1px solid #B5B3CC;" class="small"><tbody><tr class="background_dark reverse"><th colspan="7">December</th></tr><tr align="center"><th width="30">S</th><th width="30">M</th><th width="30">T</th><th width="30">W</th><th width="30">T</th><th width="30">F</th><th width="30">S</th></tr><tr align="center"><td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><a href="?d=1201">1</a></td>
<td><a href="?d=1202">2</a></td>
</tr>
<tr align="center"><td><a href="?d=1203">3</a></td>
<td><a href="?d=1204">4</a></td>
<td><a href="?d=1205">5</a></td>
<td><a href="?d=1206">6</a></td>
<td><a href="?d=1207">7</a></td>
<td><a href="?d=1208">8</a></td>
<td><a href="?d=1209">9</a></td>
</tr>
<tr align="center"><td><a href="?d=1210">10</a></td>
<td><a href="?d=1211">11</a></td>
<td><a href="?d=1212">12</a></td>
<td><a href="?d=1213">13</a></td>
<td><a href="?d=1214">14</a></td>
<td><a href="?d=1215">15</a></td>
<td><a href="?d=1216">16</a></td>
</tr>
<tr align="center"><td><a href="?d=1217">17</a></td>
<td><a href="?d=1218">18</a></td>
<td><a href="?d=1219">19</a></td>
<td><a href="?d=1220">20</a></td>
<td><a href="?d=1221">21</a></td>
<td><a href="?d=1222">22</a></td>
<td><a href="?d=1223">23</a></td>
</tr>
<tr align="center"><td><a href="?d=1224">24</a></td>
<td><a href="?d=1225">25</a></td>
<td><a href="?d=1226">26</a></td>
<td><a href="?d=1227">27</a></td>
<td><a href="?d=1228">28</a></td>
<td><a href="?d=1229">29</a></td>
<td><a href="?d=1230">30</a></td>
</tr>
<tr align="center"><td><a href="?d=1231">31</a></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody></table>
</div>
</div>"""



tree = html.fromstring(html_list)
	#print(page.text)
date_list = tree.xpath('//a/@href')
print(date_list)







