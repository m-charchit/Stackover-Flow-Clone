-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2021 at 12:38 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `ans_no` int(11) NOT NULL,
  `answer` mediumtext DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `votes` int(11) DEFAULT NULL,
  `real_answer` varchar(5) DEFAULT NULL,
  `date` varchar(15) DEFAULT NULL,
  `ques_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`ans_no`, `answer`, `username`, `votes`, `real_answer`, `date`, `ques_id`) VALUES
(4, '<p>try answer 3 </p>\r\n<p> </p>', 'charchit', 0, 'true', '2021-06-17 13:0', 6),
(5, '<p>answertest12345</p>\r\n<p> </p>', 'charchit', 1, 'false', '2021-06-17 14:2', 14),
(6, '<pre><code>if (response == \"login\"){</code><br /><br /><code>        document.location.reload()</code><br /><br /><code>      } </code></pre>', 'charchit', 0, 'false', '2021-06-18 00:0', 6),
(14, '<pre><code>&lt;!doctype html&gt;</code><br /><br /><code>&lt;html lang=\"en\"&gt;</code><br /><br /><code>  &lt;head&gt;</code><br /><br /><code>    &lt;!-- Required meta tags --&gt;</code><br /><br /><code>    &lt;meta charset=\"utf-8\"&gt;</code><br /><br /><code>    &lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\"&gt;</code><br /><br /><code>    &lt;link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.6.3/css/all.css\" integrity=\"sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/\" crossorigin=\"anonymous\"&gt;</code><br /><br /><code>    &lt;script src=\"https://cdn.tiny.cloud/1/68rymc29tevtihzfrcfmvg6k14gxllt1ri28lawyvj4nz9mt/tinymce/5/tinymce.min.js\" referrerpolicy=\"origin\"&gt;&lt;/script&gt;</code><br /><br /><code>        &lt;script&gt;</code><br /><br /><code>        tinymce.init({</code><br /><br /><code>            selector: \'.textarea\',</code><br /><br /><code>            inline:true, </code><br /><br /><code>            menubar: \"edit format insert\",</code><br /><br /><code>            plugins:\"link lists \",</code><br /><br /><code>            toolbar: \'undo redo  | bold italic | link \', </code><br /><br /><code>            height: \"200\" </code><br /><br /><code>        });</code><br /><br /><code>        tinymce.init({</code><br /><br /><code>            selector: \'#mytextarea\',</code><br /><br /><code>            height: \"420\", </code><br /><br /><code>            plugins: \'help advlist link image lists code media\', </code><br /><br /><code>            entity_encoding: \"raw\",</code><br /><br /><code>        });    </code><br /><br /><code>        &lt;/script&gt;</code><br /><br /><code>    &lt;!-- Bootstrap CSS --&gt;</code><br /><br /><code>    &lt;!-- &lt;link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css\" integrity=\"sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l\" crossorigin=\"anonymous\"&gt; --&gt;</code><br /><br /><code>    &lt;link rel=\"stylesheet\" href=\"/static/bootstrap/css/bootstrap.min.css\"&gt;</code><br /><br /><code>    &lt;link href=\"https://cdn.datatables.net/1.10.24/css/jquery.dataTables.css\" rel=\"stylesheet\" type=\"text/css\"&gt;</code><br /><br /><code>    &lt;link rel=\"stylesheet\" href=\"/static/style.css\"&gt;</code><br /><br /><code>    &lt;script src=\"https://code.jquery.com/jquery-3.1.0.js\" &gt;&lt;/script&gt;</code><br /><br /><code>    &lt;title&gt;Hello, world!&lt;/title&gt;</code><br /><br /><code>    &lt;style&gt;.dropdown:hover&gt;.dropdown-menu {</code><br /><br /><code>        display: block;</code><br /><br /><code>      }&lt;/style&gt;</code><br /><br /><code>  &lt;/head&gt;</code><br /><br /><br /><br /><br /><code>  &lt;body&gt;</code><br /><br /><code>&lt;nav class=\"navbar navbar-expand-md navbar-dark navbar-custom fixed-top\" style=\"    background-color: #7952b3;</code><br /><br /><code>    color: white;\"&gt;</code><br /><br /><code>        &lt;a class=\"navbar-brand\" href=\"#\"&gt;stackover flow 2.0&lt;/a&gt;</code><br /><br /><code>        &lt;button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarColor01\" aria-controls=\"navbarColor01\" aria-expanded=\"false\" aria-label=\"Toggle navigation\"&gt;</code><br /><br /><code>            &lt;span class=\"navbar-toggler-icon\"&gt;&lt;/span&gt;</code><br /><br /><code>        &lt;/button&gt;</code><br /><br /><code>        &lt;div class=\"collapse navbar-collapse\" id=\"navbarColor01\"&gt;</code><br /><br /><code>            &lt;ul class=\"navbar-nav mr-auto\"&gt;</code><br /><br /><code>                &lt;li class=\"nav-item\"&gt;</code><br /><br /><code>                    &lt;a class=\"nav-link\" href=\"/\"&gt;Home&lt;/a&gt;</code><br /><br /><code>                &lt;/li&gt;</code><br /><br /><code>                </code><br /><br /><code>               </code><br /><br /><code>                </code><br /><br /><code>                &lt;li class=\"nav-item\"&gt;</code><br /><br /><code>                    &lt;a class=\"nav-link\" href=\"/signin\"&gt;Sign in</code><br /><br /><code>                    &lt;/a&gt;</code><br /><br /><code>                &lt;/li&gt;</code><br /><br /><code>                </code><br /><br /><code>                &lt;li class=\"nav-item\"&gt;</code><br /><br /><code>                    &lt;a class=\"nav-link\" href=\"/signup\"&gt;sign Up&lt;/a&gt;</code><br /><br /><code>                &lt;/li&gt;</code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>        &lt;/ul&gt;</code><br /><br /><code>        &lt;form class=\"form-inline\" method=\"get\" action=\"/search\"&gt;</code><br /><br /><code>            &lt;input class=\"form-control mr-sm-2\" type=\"search\" name=\"query\" placeholder=\"[tag] or question\" aria-label=\"Search\"&gt;</code><br /><br /><code>            &lt;button class=\"btn btn-outline-info my-2 my-sm-0\" type=\"submit\" style=\"    color: white;</code><br /><br /><code>    border-color: white;\"&gt;Search&lt;/button&gt;</code><br /><br /><code>            &lt;/form&gt;</code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>        </code><br /><br /><code>    &lt;/nav&gt;</code><br /><br /><code>    &lt;br&gt;</code><br /><br /><code>    &lt;br&gt;</code><br /><br /><code>    &lt;br&gt;</code><br /><br /><br /><br /><br /><code>    </code><br /><br /><code>    </code><br /><br /><code>&lt;script&gt;</code><br /><br /><code>    function url_manager(key,value){</code><br /><br /><code>        const url = new URL(window.location.href);</code><br /><br /><code>        url.searchParams.set(key,value );</code><br /><br /><code>        window.location.replace(url)</code><br /><br /><code>    } </code><br /><br /><code>    function load_more(ids,myid,myclass){</code><br /><br /><code>        console.log(ids)</code><br /><br /><code>        $(\'div\').filter(function() {</code><br /><br /><br /><br /><br /><code>        return parseInt( this.id.replace(`${myid}-`,\'\'), 10) &gt; 5;</code><br /><br /><code>      }).hide();</code><br /><br /><code>      $(\'hr\').filter(function() {</code><br /><br /><code>        return parseInt( this.className.replace(`${myclass}-`,\'\'), 10) &gt; 5;</code><br /><br /><code>        }).hide();</code><br /><br /><code>      </code><br /><br /><code>      $(`.${ids}`).click(function (){ </code><br /><br /><code>          $(this).prevAll().show()</code><br /><br /><code>            $(this).hide()</code><br /><br /><code>        })}</code><br /><br /><code>&lt;/script&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><code>&lt;div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\"&gt;</code><br /><br /><code>    Login To Continue</code><br /><br /><code>    &lt;button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"&gt;</code><br /><br /><code>        &lt;span aria-hidden=\"true\"&gt;&amp;times;&lt;/span&gt;</code><br /><br /><code>    &lt;/button&gt;</code><br /><br /><code>&lt;/div&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><code>        &lt;input type=\"text\" id=\"link\" style=\"position:relative;top: -4000px;</code><br /><br /><code>            left:-4000px\"&gt;</code><br /><br /><code>        &lt;div class=\"container\"&gt;</code><br /><br /><code>            &lt;h2 class=\"title-ques\"&gt;</code><br /><br /><code>                &lt;a style=\"color:black;\" href=\"/14/histroy\"&gt;histroy&lt;/a&gt;</code><br /><br /><code>                &lt;div class=\"edit-delete\"&gt;</code><br /><br /><code>                    </code><br /><br /><code>                &lt;button type=\"button\" id=\"share\" class=\"btn btn-sm btn-primary\"</code><br /><br /><code>                    data-container=\"body\" data-toggle=\"popover\"</code><br /><br /><code>                    data-placement=\"right\" data-content=\"Link Copied!!\"&gt;</code><br /><br /><code>                    Share</code><br /><br /><code>                &lt;/button&gt;</code><br /><br /><br /><br /><br /><code>            &lt;/div&gt;</code><br /><br /><br /><br /><br /><code>        &lt;/h2&gt;</code><br /><br /><code>        &lt;hr&gt;</code><br /><br /><code>        &lt;div class=\"grid_ques\"&gt;</code><br /><br /><code>            </code><br /><br /><code>        &lt;div style=\"grid-column:1; margin-right: 10px\"&gt; &lt;div class=\"vote\"&gt;</code><br /><br /><code>            </code><br /><br /><code>                </code><br /><br /><code>            &lt;span class=\"up-vote\" id=\"\" style=\"color:\" &gt;&lt;i class=\"fas fa-angle-up\" &gt;&lt;/i&gt;&lt;/span&gt;</code><br /><br /><code>            &lt;span class=\"number\" id=\"number_14\"&gt;1&lt;/span&gt;</code><br /><br /><code>            &lt;span class=\"down-vote\" style=\'color:\'&gt;&lt;i class=\"fas fa-angle-down\" &gt;&lt;/i&gt;&lt;/span&gt;</code><br /><br /><code>          &lt;/div&gt;&lt;/div&gt;</code><br /><br /><code>        &lt;div style=\"grid-column:2\"&gt;&lt;p&gt;whho was gissuepe garibaldi&lt;/p&gt;</code><br /><br /><code>        &lt;div class=\"row\"&gt;</code><br /><br /><code>            &lt;div class=\"col\"&gt;</code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><br /><br /><br /><code>                &lt;p class=\"tag ptag\"&gt;&lt;a href=\"/tag/history\"&gt;history&lt;/a&gt; &lt;/p&gt;</code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><br /><br /><br /><code>                &lt;p class=\"tag ptag\"&gt;&lt;a href=\"/tag/europe\"&gt;europe&lt;/a&gt; &lt;/p&gt;</code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><code>            &lt;/div&gt;</code><br /><br /><code>            &lt;div class=\"col\"&gt;</code><br /><br /><code>                &lt;p class=\"user\"&gt;</code><br /><br /><code>                    &lt;a href=\"/profile/chirag\" class=\"user-a\"&gt;chirag&lt;/a&gt;</code><br /><br /><code>                    &lt;br&gt;</code><br /><br /><code>                    &lt;span class=\"Date\"&gt;</code><br /><br /><code>                        2021-05-20 13:34:46</code><br /><br /><code>                    &lt;/span&gt;</code><br /><br /><code>                &lt;/p&gt;</code><br /><br /><code>            &lt;/div&gt;</code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>    </code><br /><br /><code>        &lt;button class=\"link-btn btns\" type=\"button\" data-toggle=\"collapse\"</code><br /><br /><code>            data-target=\"#question\" aria-expanded=\"false\"</code><br /><br /><code>            aria-controls=\"collapseExample\"&gt;</code><br /><br /><code>            Add comment</code><br /><br /><code>        &lt;/button&gt;</code><br /><br /><code>    &lt;/div&gt;</code><br /><br /><code>&lt;/div&gt;</code><br /><br /><code>        &lt;div class=\"container\" style=\"font-size: 13px; line-height: 18px;\"&gt;</code><br /><br /><code>            &lt;hr style=\"margin-top: 0.3rem; margin-bottom:0.3rem;\"&gt;</code><br /><br /><br /><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><br /><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>        </code><br /><br /><code>&lt;div class=\"container\"&gt;</code><br /><br /><code>    &lt;div class=\"collapse\" id=\"question\"&gt;</code><br /><br /><code>        &lt;div class=\"card card-body\"&gt;</code><br /><br /><code>            &lt;form action=\"/comment\" method=\"post\"&gt;</code><br /><br /><code>                &lt;textarea name=\"comment\" style=\"display:none;\" class=\"text-sub\"&gt;&lt;/textarea&gt;</code><br /><br /><code>                &lt;div class=\"textarea form-control\" &gt;&lt;/div&gt;</code><br /><br /><code>                &lt;input type=\"hidden\" name=\"sno\" value=\"14\"&gt;</code><br /><br /><code>                &lt;button type=\"submit\" class=\"btn btn-primary comm\"</code><br /><br /><code>                    style=\"margin-top:20px\"&gt;Post comment&lt;/button&gt;</code><br /><br /><code>            &lt;/form&gt;</code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>    &lt;/div&gt;</code><br /><br /><code>&lt;/div&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><code>        </code><br /><br /><code>        </code><br /><br /><code>        </code><br /><br /><code>&lt;h4 style=\"margin-bottom:-26px;\"&gt;1 Answers&lt;/h4&gt;</code><br /><br /><code>    &lt;button style=\"float:right; margin-left:5px;\" class=\"oldest btn</code><br /><br /><code>        btn-sm btn-primary\"&gt;oldest&lt;/button&gt;</code><br /><br /><code>    &lt;button style=\"float:right; margin-left:5px;\" class=\"oldest btn</code><br /><br /><code>        btn-sm btn-primary\"&gt;latest&lt;/button&gt;</code><br /><br /><code>        &lt;script&gt;</code><br /><br /><code>            $(\".oldest\").click(function (e) {</code><br /><br /><code>                url_manager(\"tab\",$(this).text())</code><br /><br /><code>            })</code><br /><br /><code>        &lt;/script&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><code>        &lt;hr&gt;</code><br /><br /><code>        </code><br /><br /><code>        </code><br /><br /><code>        &lt;div class=\"grid_ques my_an\"&gt;</code><br /><br /><code>            &lt;div style=\"grid-column:1\"&gt;&lt;div class=\"vote\"&gt;</code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><code>                &lt;span class=\"up-vote\" id=\"\" style=\"color:\"&gt;&lt;i class=\"fas fa-angle-up\"&gt;&lt;/i&gt;&lt;/span&gt;</code><br /><br /><code>                &lt;span class=\"number\" id=\"number_5\" &gt;1&lt;/span&gt;</code><br /><br /><code>                &lt;span class=\"down-vote\"style=\"color:\"&gt;&lt;i class=\"fas fa-angle-down\"&gt;&lt;/i&gt;&lt;/span&gt;</code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><code>                </code><br /><br /><code>              &lt;/div&gt;&lt;/div&gt;</code><br /><br /><code>        &lt;div class=\"container\" style=\"grid-column:2\" id=\"a5\"&gt;</code><br /><br /><code>            &lt;div id=\"tinymce\" class=\"mce-content-body\"data-id=\"mce_7\"</code><br /><br /><code>                contenteditable=\"false\" spellcheck=\"false\"</code><br /><br /><code>                style=\"line-height:20px;\"&gt;</code><br /><br /><code>                &lt;p&gt;answertest12345&lt;/p&gt;</code><br /><br /><code>&lt;p&gt; &lt;/p&gt;</code><br /><br /><code>            &lt;/div&gt;</code><br /><br /><code>            &lt;div class=\"row\"&gt;</code><br /><br /><code>                &lt;div class=\"col\"&gt;</code><br /><br /><code>                    </code><br /><br /><code>                    &lt;button class=\"link-btn btns share\" id=\"#a5\"</code><br /><br /><code>                        data-container=\"body\" data-toggle=\"popover\"</code><br /><br /><code>                        data-placement=\"right\" data-content=\"Link Copied!!\"&gt;</code><br /><br /><code>                        Share</code><br /><br /><code>                    &lt;/button&gt;</code><br /><br /><code>                &lt;/div&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><code>                &lt;div class=\"col\"&gt;</code><br /><br /><br /><br /><br /><code>                    &lt;div class=\"user\"&gt;</code><br /><br /><code>                        &lt;a href=\"/profile/charchit\" class=\"user-a\"&gt;charchit&lt;/a&gt;</code><br /><br /><code>                        &lt;br&gt;</code><br /><br /><code>                        &lt;span class=\"Date\"&gt;</code><br /><br /><code>                            2021-06-17 14:2</code><br /><br /><code>                        &lt;/span&gt;</code><br /><br /><code>                    &lt;/div&gt;</code><br /><br /><br /><br /><br /><code>                &lt;/div&gt;</code><br /><br /><code>            &lt;/div&gt;</code><br /><br /><code>            &lt;button class=\"link-btn btns\" type=\"button\" data-toggle=\"collapse\"</code><br /><br /><code>                data-target=\"#e5\" aria-expanded=\"false\"</code><br /><br /><code>                aria-controls=\"collapseExample\"&gt;</code><br /><br /><code>                Add comment</code><br /><br /><code>            &lt;/button&gt;</code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>&lt;/div&gt;</code><br /><br /><code>        &lt;div class=\"container\" style=\"font-size: 13px; line-height: 18px;\"&gt;</code><br /><br /><code>            &lt;hr style=\"margin-top: 0.3rem; margin-bottom:0.3rem;\"&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><br /><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>            </code><br /><br /><code>&lt;div class=\"container\"&gt;</code><br /><br /><code>    &lt;div class=\"collapse\" id=\"e5\"&gt;</code><br /><br /><code>        &lt;div class=\"card card-body\"&gt;</code><br /><br /><code>            &lt;form action=\"/comment\" method=\"post\"&gt;</code><br /><br /><code>                &lt;textarea name=\"comment\" style=\"display:none;\" class=\"text-sub\"&gt;&lt;/textarea&gt;</code><br /><br /><code>                &lt;div class=\"textarea form-control\" &gt;&lt;/div&gt;</code><br /><br /><code>                &lt;input type=\"hidden\" name=\"sno\" value=\"5\"&gt;</code><br /><br /><code>                &lt;button type=\"submit\" class=\"btn btn-primary comm\"</code><br /><br /><code>                    style=\"margin-top:20px\"&gt;Post comment&lt;/button&gt;</code><br /><br /><code>            &lt;/form&gt;</code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>    &lt;/div&gt;</code><br /><br /><code>&lt;/div&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><code>        &lt;hr style=\"margin-top: 2rem !important;\"&gt;</code><br /><br /><code>        </code><br /><br /><br /><br /><br /><code>        </code><br /><br /><br /><br /><br /><code>        &lt;form action=\"/14/histroy/\" method=\"post\"&gt;</code><br /><br /><code>            &lt;div class=\"form-group\" style=\"padding:0px 70px;\"&gt;</code><br /><br /><br /><br /><br /><code>                &lt;label for=\"exampleFormControlTextarea1\"&gt;Your Answer&lt;/label&gt;</code><br /><br /><code>                &lt;textarea name=\"answer\" class=\"form-control\" id=\"mytextarea\"</code><br /><br /><code>                    rows=\"6\"</code><br /><br /><code>                    style=\"margin:10px; border-radius:10px;\"&gt;&lt;/textarea&gt;</code><br /><br /><code>                &lt;button type=\"submit\" class=\"btn btn-primary\"</code><br /><br /><code>                    style=\"margin:10px;\"&gt;Post Answer&lt;/button&gt;</code><br /><br /><code>            &lt;/div&gt;</code><br /><br /><br /><br /><br /><code>        &lt;/form&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><code>    &lt;/div&gt;</code><br /><br /><br /><br /><br /><code>    </code><br /><br /><br /><br /><br /><br /><br /><br /><code>    </code><br /><br /><code>    &lt;button class=\"scroll btn btn-primary\" type=\"button\"&gt;&lt;i class=\"fas fa-angle-up\" &gt;&lt;/i&gt;&lt;/button&gt;</code><br /><br /><code>    &lt;!-- footer --&gt;</code><br /><br /><code>    &lt;div class=\"container\"&gt;</code><br /><br /><code>    &lt;footer&gt;</code><br /><br /><code>            &lt;div class=\"row\"&gt;</code><br /><br /><code>                &lt;div class=\"col-lg-8 col-md-10 mx-auto\"&gt;</code><br /><br /><code>                    &lt;ul class=\"list-inline text-center\"&gt;</code><br /><br /><code>                        &lt;li class=\"list-inline-item\"&gt;</code><br /><br /><code>                            &lt;a href=\"#!\"&gt;</code><br /><br /><code>                                &lt;span class=\"fa-stack fa-lg\"&gt;</code><br /><br /><code>                                    &lt;i class=\"fas fa-circle fa-stack-2x\"&gt;&lt;/i&gt;</code><br /><br /><code>                                    &lt;i class=\"fab fa-twitter fa-stack-1x fa-inverse\"&gt;&lt;/i&gt;</code><br /><br /><code>                                &lt;/span&gt;</code><br /><br /><code>                            &lt;/a&gt;</code><br /><br /><code>                        &lt;/li&gt;</code><br /><br /><code>                        &lt;li class=\"list-inline-item\"&gt;</code><br /><br /><code>                            &lt;a href=\"#!\"&gt;</code><br /><br /><code>                                &lt;span class=\"fa-stack fa-lg\"&gt;</code><br /><br /><code>                                    &lt;i class=\"fas fa-circle fa-stack-2x\"&gt;&lt;/i&gt;</code><br /><br /><code>                                    &lt;i class=\"fab fa-facebook-f fa-stack-1x fa-inverse\"&gt;&lt;/i&gt;</code><br /><br /><code>                                &lt;/span&gt;</code><br /><br /><code>                            &lt;/a&gt;</code><br /><br /><code>                        &lt;/li&gt;</code><br /><br /><code>                        &lt;li class=\"list-inline-item\"&gt;</code><br /><br /><code>                            &lt;a href=\"#!\"&gt;</code><br /><br /><code>                                &lt;span class=\"fa-stack fa-lg\"&gt;</code><br /><br /><code>                                    &lt;i class=\"fas fa-circle fa-stack-2x\"&gt;&lt;/i&gt;</code><br /><br /><code>                                    &lt;i class=\"fab fa-github fa-stack-1x fa-inverse\"&gt;&lt;/i&gt;</code><br /><br /><code>                                &lt;/span&gt;</code><br /><br /><code>                            &lt;/a&gt;</code><br /><br /><code>                        &lt;/li&gt;</code><br /><br /><code>                    &lt;/ul&gt;</code><br /><br /><code>                    &lt;p class=\"copyright text-center \"&gt;Copyright &amp;copy; charchit&lt;/p&gt;</code><br /><br /><code>                &lt;/div&gt;</code><br /><br /><code>            &lt;/div&gt;</code><br /><br /><code>        &lt;/footer&gt;</code><br /><br /><code>        &lt;/div&gt;</code><br /><br /><code>        &lt;!-- &lt;script src=\"https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns\" crossorigin=\"anonymous\"&gt;&lt;/script&gt; --&gt;</code><br /><br /><code>        &lt;script src=\"/static/bootstrap/js/bootstrap.bundle.js\"&gt;&lt;/script&gt;</code><br /><br /><code>        </code><br /><br /><code>    &lt;script&gt;</code><br /><br /><code>        $(document).ready(function () {</code><br /><br /><code>            $(function () {</code><br /><br /><code>                $(\'[data-toggle=\"popover\"]\').popover()</code><br /><br /><code>            })</code><br /><br /><code>            $(\"#share\").click(function (){</code><br /><br /><code>                $(\"#link\").val(window.location.href);</code><br /><br /><code>                $(\"#link\").select();</code><br /><br /><code>                document.execCommand(\"copy\");</code><br /><br /><code>                $(\"#link\").val(\"\");</code><br /><br /><code>            })</code><br /><br /><code>            $(document).on(\"click\",\".share\",function (e){</code><br /><br /><code>                loc = window.location.href ? window.location.href.split(\"#\")[0] : window.location.href;</code><br /><br /><code>                $(\"#link\").val(`${loc}${e.target.id}`);</code><br /><br /><code>                $(\"#link\").select();</code><br /><br /><code>                document.execCommand(\"copy\");</code><br /><br /><code>                $(\"#link\").val(\"\");</code><br /><br /><code>                </code><br /><br /><code>            })</code><br /><br /><code>            console.log(window.location.href.toString().includes(\"/ques/\"))</code><br /><br /><code>            if ( window.location.href.toString().includes(\"/ques/\") ){</code><br /><br /><code>               </code><br /><br /><code>            a = $(\"#tagedit\").val().trim()</code><br /><br /><code>            $(\"#tagedit\").val(a)</code><br /><br /><code>            }</code><br /><br /><code>            $(\".page-link\").click(function (e){</code><br /><br /><code>                url_manager(\"no_of_ques\",$(this).text())</code><br /><br /><code>                </code><br /><br /><code>            })</code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><code>            </code><br /><br /><br /><br /><br /><code>            $(\".textarea\").on(\"input\",function(){</code><br /><br /><code>                $(this).prev().val($(this).text())</code><br /><br /><code>                console.log($(this).prev().val())</code><br /><br /><code>            })</code><br /><br /><code>            </code><br /><br /><code>            if ( window.location.pathname.endsWith(\"/search/\") &amp;&amp; !window.location.search){</code><br /><br /><code>                window.location.replace(\"/\")</code><br /><br /><code>            }</code><br /><br /><code>    </code><br /><br /><code>        })</code><br /><br /><code>        </code><br /><br /><code>    &lt;/script&gt;</code><br /><br /><code>    </code><br /><br /><code>    </code><br /><br /><code>        </code><br /><br /><code>                &lt;script&gt;</code><br /><br /><code>                        load_more(\"load\",\"myid\",\"myclass\")</code><br /><br /><code>                    &lt;/script&gt;</code><br /><br /><code>                </code><br /><br /><code>    &lt;script src=\"/static/app.js\"&gt;&lt;/script&gt;</code><br /><br /><br /><br /><br /><code>&lt;script&gt;</code><br /><br /><code>    $(window).scroll(function(){</code><br /><br /><code>        if (this.scrollY &gt; 400){</code><br /><br /><code>        $(\".scroll\").fadeIn()</code><br /><br /><code>    }</code><br /><br /><code>    else{</code><br /><br /><code>        $(\".scroll\").fadeOut()</code><br /><br /><br /><br /><br /><code>    }</code><br /><br /><br /><br /><br /><code>})</code><br /><br /><code>$(\".scroll\").click(function (e){</code><br /><br /><code>    window.scroll({</code><br /><br /><code>        top:0,</code><br /><br /><code>        left:0,</code><br /><br /><code>        behavior:\"smooth\"</code><br /><br /><code>    })</code><br /><br /><br /><br /><br /><code>})</code><br /><br /><code>&lt;/script&gt;</code><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><code>&lt;/body&gt;</code><br /><br /><code>&lt;/html&gt;</code><br /><br /><br /></pre>', 'charchit', 0, 'false', '2021-06-18 01:2', 6);

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `comm_sno` int(11) NOT NULL,
  `sno` int(11) DEFAULT NULL,
  `ques_sno` int(11) DEFAULT 0,
  `comment` varchar(500) NOT NULL,
  `username` varchar(30) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`comm_sno`, `sno`, `ques_sno`, `comment`, `username`, `date`) VALUES
(1, 2, NULL, 'comment test', 'charchit', '2021-06-17 12:59:02');

-- --------------------------------------------------------

--
-- Table structure for table `detail`
--

CREATE TABLE `detail` (
  `username` varchar(20) NOT NULL,
  `email` varchar(25) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `detail`
--

INSERT INTO `detail` (`username`, `email`, `password`, `date`) VALUES
('charchit', 'charchit.dahiya@gmail.com', 'a', '2021-05-18 00:26:29'),
('chirag', 'charchit.dahiya@gmail.com', 'a', '2021-05-18 06:28:11');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `sno` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `body` varchar(3000) NOT NULL,
  `tag` varchar(60) NOT NULL,
  `username` varchar(20) NOT NULL,
  `upvote` int(11) NOT NULL DEFAULT 0,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`sno`, `title`, `body`, `tag`, `username`, `upvote`, `date`) VALUES
(3, 'how to make a stack over flow clone using flask', '<p>Hi I am making a stack over flow clone. But I don\'t know where to start from.. I even don\'t know what should b ethe app name. any ideas of how can i start building my project.</p>\r\n<p> </p>\r\n<p>Edit : Hey I amde halp of it.</p>', 'project ideas flask', 'charchit', 0, '2021-05-18 00:59:57'),
(5, 'I stole this question from stackover flow clone', '<p>After coming back to my own question after 5 year and seeing so many people found this useful, a little update. A string variable can be split into a list by using the split function (it can contain similar values, set is for the assignment) . I haven\'t found this function in the official documentation but it works similar to normal Python. The items can be called via an index, used in a loop or like Dave suggested if you know the values, it can set variables like a tuple. </p>\r\n<p><code>{% set list1 = variable1.split(\';\') %} The grass is {{ list1[0] }} and the boat is {{ list1[1] }} or {% set list1 = variable1.split(\';\') %} {% for item in list1 %}</code></p>\r\n<p><code>{{ item }}</code></p>\r\n<p><code>{% endfor %} or {% set item1, item2 = variable1.split(\';\') %} The grass is {{ item1 }} and the boat is {{ item2 }}</code></p>', 'python', 'charchit', 0, '2021-05-18 03:25:54'),
(6, 'Split string into list in jinja  ', '<p>have some variables in a jinja2 template which are strings seperated by a \';\'.</p>\r\n<p>I need to use these strings separately in the code. i.e. the variable is</p>\r\n<p><code>variable1 = \"green;blue\" {% list1 = {{ variable1 }}.split(\';\') %} The grass is {{ list1[0] }} and the boat is {{ list1[1] }}</code></p>\r\n<p>I can split them up before rendering the template but since it are sometimes up to 10 strings inside the string this gets messy.</p>\r\n<p>I had a jsp before where I did:</p>\r\n<p><code>&lt;% String[] list1 = val.get(\"variable1\").split(\";\");%&gt; The grass is &lt;%= list1[0] %&gt; and the boat is &lt;%= list1[1] <sub>%&gt;</sub></code></p>\r\n<p>EDIT: It works with:</p>\r\n<p><code>{% set list1 = variable1.split(\';\') %} The grass is {{ list1[0] }} and the boat is {{ list1[1] }}</code></p>', ' flask  ', 'charchit', 1, '2021-05-18 03:26:38'),
(7, 'how does bootstrap works', '<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-primary\"&gt;Primary&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-secondary\"&gt;Secondary&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-success\"&gt;Success&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-danger\"&gt;Danger&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-warning\"&gt;Warning&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-info\"&gt;Info&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-light\"&gt;Light&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-dark\"&gt;Dark&lt;/button&gt;</span></code></p>\r\n<p><code><span style=\"font-family: monospace;\"> </span></code></p>\r\n<p><code><span style=\"font-family: monospace;\">&lt;button type=\"button\" class=\"btn btn-link\"&gt;Link&lt;/button&gt;</span></code></p>', 'bootstrap 4', 'charchit', 0, '2021-05-18 03:27:05'),
(12, 'I am chirag new to this Website. Please tell me what to do.', 'I want to ask question but don\'t know how , please tell me how to ask the question here\r\nlike the below\r\nI want to click a table element and to have it do x the first click and if clicked again perform Y\r\n\r\n<td class=\'p\' id=\'e1\' onclick=\"myFunction2()\"><img src=\'person2.png\'/></td>\r\nThats what I have for my HTML for one click just now, but I wish to change that so that an item can be selected, then if clicked again for a deselect it would then trigger a different function.\r\n\r\njavascript', ' javascript ', 'chirag', 0, '2021-05-18 06:29:45'),
(14, 'histroy', '<p>whho was gissuepe garibaldi</p>', ' history europe ', 'chirag', 1, '2021-05-20 13:34:46'),
(15, 'how to create a customized 404 page in Flask.', '<p><img style=\"display: block; margin-left: auto; margin-right: auto;\" src=\"https://www.w3schools.com/images/w3lynx_200.png\" alt=\"\" width=\"120\" height=\"200\" /></p>\r\n<p>@app.errorhandler(404) def page_not_found(error): return render_template(\'404.html\', title = \'404\'), 404 if something wrong: abort(404) I read this but I want to know if there is any other method . <br />Also The bunny is cute , isn\'t it?</p>', 'flask python error e bunny', 'charchit', 1, '2021-05-25 03:48:01');

-- --------------------------------------------------------

--
-- Table structure for table `vote`
--

CREATE TABLE `vote` (
  `sno` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `no` int(11) NOT NULL,
  `votetype` varchar(10) NOT NULL,
  `aq_vote` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vote`
--

INSERT INTO `vote` (`sno`, `username`, `no`, `votetype`, `aq_vote`) VALUES
(11, 'charchit', 15, 'upvote', 'ques'),
(22, 'charchit', 29, 'upvote', 'answer'),
(23, 'charchit', 6, 'downvote', 'ques'),
(24, 'charchit', 25, 'upvote', 'answer'),
(25, 'charchit', 20, 'downvote', 'answer'),
(26, 'charchit', 2, 'downvote', 'answer'),
(27, 'charchit', 30, 'downvote', 'answer'),
(28, 'charchit', 5, 'upvote', 'answer'),
(29, 'charchit', 14, 'upvote', 'ques'),
(31, 'charchit', 16, 'upvote', 'answer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`ans_no`),
  ADD KEY `ques_id` (`ques_id`);
ALTER TABLE `answers` ADD FULLTEXT KEY `answer` (`answer`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`comm_sno`);

--
-- Indexes for table `detail`
--
ALTER TABLE `detail`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`sno`);
ALTER TABLE `question` ADD FULLTEXT KEY `title` (`title`,`body`,`tag`);
ALTER TABLE `question` ADD FULLTEXT KEY `title_2` (`title`,`body`);
ALTER TABLE `question` ADD FULLTEXT KEY `title_3` (`title`,`body`);

--
-- Indexes for table `vote`
--
ALTER TABLE `vote`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `ans_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `comm_sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `vote`
--
ALTER TABLE `vote`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`ques_id`) REFERENCES `question` (`sno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
