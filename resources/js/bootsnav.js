(function (a) {
    var b = {
        initialize: function () {
            this.event();
            this.hoverDropdown();
            this.navbarSticky()
        },
        event: function () {
            var i = a("nav.navbar.bootsnav");
            var d = i.hasClass("navbar-sticky");
            if (d) {
                i.wrap("<div class='wrap-sticky'></div>")
            }
            if (i.hasClass("brand-center")) {
                var k = new Array(),
                    g = a("nav.brand-center"),
                    c = g.find("ul.navbar-nav");
                g.find("ul.navbar-nav > li").each(function () {
                    k.push(a(this).html())
                });
                var e = k.splice(0, Math.round(k.length / 2)),
                    f = k,
                    j = "";
                var h = function (m) {
                    j = "";
                    for (var l = 0; l < m.length; l++) {
                        j += "<li>" + m[l] + "</li>"
                    }
                };
                h(e);
                c.html(j);
                g.find("ul.nav").first().addClass("navbar-left");
                h(f);
                c.after('<ul class="nav navbar-nav"></ul>').next().html(j);
                g.find("ul.nav").last().addClass("navbar-right");
                g.find("ul.nav.navbar-left").wrap("<div class='col-half left'></div>");
                g.find("ul.nav.navbar-right").wrap("<div class='col-half right'></div>");
                g.find("ul.navbar-nav > li").each(function () {
                    var m = a("ul.dropdown-menu", this),
                        l = a("ul.megamenu-content", this);
                    m.closest("li").addClass("dropdown");
                    l.closest("li").addClass("megamenu-fw")
                })
            }
            if (i.hasClass("navbar-sidebar")) {
                a("body").addClass("wrap-nav-sidebar");
                i.wrapInner("<div class='scroller'></div>")
            } else {
                a(".bootsnav").addClass("on")
            }
            if (i.find("ul.nav").hasClass("navbar-center")) {
                i.addClass("menu-center")
            }
            if (i.hasClass("navbar-full")) {
                a("nav.navbar.bootsnav").find("ul.nav").wrap("<div class='wrap-full-menu'></div>");
                a(".wrap-full-menu").wrap("<div class='nav-full'></div>");
                a("ul.nav.navbar-nav").prepend("<li class='close-full-menu'><a href='#'><i class='fa fa-times'></i></a></li>")
            } else {
                if (i.hasClass("navbar-mobile")) {
                    i.removeClass("no-full")
                } else {
                    i.addClass("no-full")
                }
            }
            if (i.hasClass("navbar-mobile")) {
                a(".navbar-collapse").on("shown.bs.collapse", function () {
                    a("body").addClass("side-right")
                });
                a(".navbar-collapse").on("hide.bs.collapse", function () {
                    a("body").removeClass("side-right")
                });
                a(window).on("resize", function () {
                    a("body").removeClass("side-right")
                })
            }
            /*if (i.hasClass("no-background")) {
                a(window).on("scroll", function () {
                    var l = a(window).scrollTop();
                    if (l > 50) {
                        a(".navbar-fixed").removeClass("no-background")
                    } else {
                        a(".navbar-fixed").addClass("no-background")
                    }
                })
            }
            if (i.hasClass("navbar-transparent")) {
                a(window).on("scroll", function () {
                    var l = a(window).scrollTop();
                    if (l > 34) {
                        a(".navbar-fixed").removeClass("navbar-transparent")
                    } else {
                        a(".navbar-fixed").addClass("navbar-transparent")
                    }
                })
            }*/
            a(".btn-cart").on("click", function (l) {
                l.stopPropagation()
            });
            a("li.search > a").on("click", function (l) {
                l.preventDefault();
                a(".top-search").slideToggle("slow")
            });
            a("nav.navbar.bootsnav .attr-nav").each(function () {
                a("li.side-menu > a", this).on("click", function (l) {
                    l.preventDefault();
                    a("nav.navbar.bootsnav > .side").toggleClass("on");
                    a("body").toggleClass("on-side")
                })
            });
            a(".side .close-side").on("click", function (l) {
                l.preventDefault();
                a("nav.navbar.bootsnav > .side").removeClass("on");
                a("body").removeClass("on-side")
            });
            a("body").wrapInner("<div class='wrapper'></div>")
        },
        hoverDropdown: function () {
            var h = a("nav.navbar.bootsnav"),
                e = a(window).width(),
                i = a(window).height(),
                g = h.find("ul.nav").data("in"),
                c = h.find("ul.nav").data("out");
            if (e < 981) {
                a(".scroller").css("height", "auto");
                a("nav.navbar.bootsnav ul.nav").find("li.dropdown").off("mouseenter");
                a("nav.navbar.bootsnav ul.nav").find("li.dropdown").off("mouseleave");
                a("nav.navbar.bootsnav ul.nav").find(".title").off("mouseenter");
                a("nav.navbar.bootsnav ul.nav").off("mouseleave");
                a(".navbar-collapse").removeClass("animated");
                a("nav.navbar.bootsnav ul.nav").each(function () {
                    a(".dropdown-menu", this).addClass("animated");
                    a(".dropdown-menu", this).removeClass(c);
                    a("a.dropdown-toggle", this).off("click");
                    a("a.dropdown-toggle", this).on("click", function (k) {
                        k.stopPropagation();
                        a(this).closest("li.dropdown").find(".dropdown-menu").first().stop().fadeToggle().toggleClass(g);
                        a(this).closest("li.dropdown").first().toggleClass("on");
                        return false
                    });
                    a("li.dropdown", this).each(function () {
                        a(this).find(".dropdown-menu").stop().fadeOut();
                        a(this).on("hidden.bs.dropdown", function () {
                            a(this).find(".dropdown-menu").stop().fadeOut()
                        });
                        return false
                    });
                    a(".megamenu-fw", this).each(function () {
                        a(".col-menu", this).each(function () {
                            a(".content", this).addClass("animated");
                            a(".content", this).stop().fadeOut();
                            a(".title", this).off("click");
                            a(".title", this).on("click", function () {
                                a(this).closest(".col-menu").find(".content").stop().fadeToggle().addClass(g);
                                a(this).closest(".col-menu").toggleClass("on");
                                return false
                            });
                            a(".content", this).on("click", function (k) {
                                k.stopPropagation()
                            })
                        })
                    })
                });
                var f = function () {
                    a("li.dropdown", this).removeClass("on");
                    a(".dropdown-menu", this).stop().fadeOut();
                    a(".dropdown-menu", this).removeClass(g);
                    a(".col-menu", this).removeClass("on");
                    a(".col-menu .content", this).stop().fadeOut();
                    a(".col-menu .content", this).removeClass(g)
                };
                a("nav.navbar.bootsnav").on("mouseleave", function () {
                    f()
                });
                a("nav.navbar.bootsnav .attr-nav").each(function () {
                    a(".dropdown-menu", this).removeClass("animated");
                    a("li.dropdown", this).off("mouseenter");
                    a("li.dropdown", this).off("mouseleave");
                    a("a.dropdown-toggle", this).off("click");
                    a("a.dropdown-toggle", this).on("click", function (k) {
                        k.stopPropagation();
                        a(this).closest("li.dropdown").find(".dropdown-menu").first().stop().fadeToggle();
                        a(".navbar-toggle").each(function () {
                            a(".fa", this).removeClass("fa-times");
                            a(".fa", this).addClass("fa-bars");
                            a(".navbar-collapse").removeClass("in");
                            a(".navbar-collapse").removeClass("on")
                        })
                    });
                    a(this).on("mouseleave", function () {
                        a(".dropdown-menu", this).stop().fadeOut();
                        a("li.dropdown", this).removeClass("on");
                        return false
                    })
                });
                a(".navbar-toggle").each(function () {
                    a(this).off("click");
                    a(this).on("click", function () {
                        a(".fa", this).toggleClass("fa-bars");
                        a(".fa", this).toggleClass("fa-times");
                        f()
                    })
                })
            } else {
                if (e > 981) {
                    a(".scroller").css("height", i + "px");
                    if (h.hasClass("navbar-sidebar")) {
                        a("nav.navbar.bootsnav ul.nav").each(function () {
                            a("a.dropdown-toggle", this).off("click");
                            a("a.dropdown-toggle", this).on("click", function (k) {
                                k.stopPropagation()
                            });
                            a(".dropdown-menu", this).addClass("animated");
                            a("li.dropdown", this).on("mouseenter", function () {
                                a(".dropdown-menu", this).eq(0).removeClass(c);
                                a(".dropdown-menu", this).eq(0).stop().fadeIn().addClass(g);
                                a(this).addClass("on");
                                return false
                            });
                            a(".col-menu").each(function () {
                                a(".content", this).addClass("animated");
                                a(".title", this).on("mouseenter", function () {
                                    a(this).closest(".col-menu").find(".content").stop().fadeIn().addClass(g);
                                    a(this).closest(".col-menu").addClass("on");
                                    return false
                                })
                            });
                            a(this).on("mouseleave", function () {
                                a(".dropdown-menu", this).stop().removeClass(g);
                                a(".dropdown-menu", this).stop().addClass(c).fadeOut();
                                a(".col-menu", this).find(".content").stop().fadeOut().removeClass(g);
                                a(".col-menu", this).removeClass("on");
                                a("li.dropdown", this).removeClass("on");
                                return false
                            })
                        })
                    } else {
                        a("nav.navbar.bootsnav ul.nav").each(function () {
                            a("a.dropdown-toggle", this).off("click");
                            a("a.dropdown-toggle", this).on("click", function (k) {
                                k.stopPropagation()
                            });
                            a(".megamenu-fw", this).each(function () {
                                a(".title", this).off("click");
                                a("a.dropdown-toggle", this).off("click");
                                a(".content").removeClass("animated")
                            });
                            a(".dropdown-menu", this).addClass("animated");
                            a("li.dropdown", this).on("mouseenter", function () {
                                a(".dropdown-menu", this).eq(0).removeClass(c);
                                a(".dropdown-menu", this).eq(0).stop().fadeIn().addClass(g);
                                a(this).addClass("on");
                                return false
                            });
                            a("li.dropdown", this).on("mouseleave", function () {
                                a(".dropdown-menu", this).eq(0).removeClass(g);
                                a(".dropdown-menu", this).eq(0).stop().fadeOut().addClass(c);
                                a(this).removeClass("on")
                            });
                            a(this).on("mouseleave", function () {
                                a(".dropdown-menu", this).removeClass(g);
                                a(".dropdown-menu", this).eq(0).stop().fadeOut().addClass(c);
                                a("li.dropdown", this).removeClass("on");
                                return false
                            })
                        })
                    }
                    a("nav.navbar.bootsnav .attr-nav").each(function () {
                        a("a.dropdown-toggle", this).off("click");
                        a("a.dropdown-toggle", this).on("click", function (k) {
                            k.stopPropagation()
                        });
                        a(".dropdown-menu", this).addClass("animated");
                        a("li.dropdown", this).on("mouseenter", function () {
                            a(".dropdown-menu", this).eq(0).removeClass(c);
                            a(".dropdown-menu", this).eq(0).stop().fadeIn().addClass(g);
                            a(this).addClass("on");
                            return false
                        });
                        a("li.dropdown", this).on("mouseleave", function () {
                            a(".dropdown-menu", this).eq(0).removeClass(g);
                            a(".dropdown-menu", this).eq(0).stop().fadeOut().addClass(c);
                            a(this).removeClass("on")
                        });
                        a(this).on("mouseleave", function () {
                            a(".dropdown-menu", this).removeClass(g);
                            a(".dropdown-menu", this).eq(0).stop().fadeOut().addClass(c);
                            a("li.dropdown", this).removeClass("on");
                            return false
                        })
                    })
                }
            }
            if (h.hasClass("navbar-full")) {
                var j = a(window).height(),
                    d = a(window).width();
                a(".nav-full").css("height", j + "px");
                a(".wrap-full-menu").css("height", j + "px");
                a(".wrap-full-menu").css("width", d + "px");
                a(".navbar-collapse").addClass("animated");
                a(".navbar-toggle").each(function () {
                    var k = a(this).data("target");
                    a(this).off("click");
                    a(this).on("click", function (l) {
                        l.preventDefault();
                        a(k).removeClass(c);
                        a(k).addClass("in");
                        a(k).addClass(g);
                        return false
                    });
                    a("li.close-full-menu").on("click", function (l) {
                        l.preventDefault();
                        a(k).addClass(c);
                        setTimeout(function () {
                            a(k).removeClass("in");
                            a(k).removeClass(g)
                        }, 500);
                        return false
                    })
                })
            }
        },
        navbarSticky: function () {
            var d = a("nav.navbar.bootsnav"),
                f = d.hasClass("navbar-sticky");
            if (f) {
                var e = d.height();
                a(".wrap-sticky").height(e);
                var c = a(".wrap-sticky").offset().top;
                a(window).on("scroll", function () {
                    var g = a(window).scrollTop();
                    if (g > c) {
                        d.addClass("sticked")
                    } else {
                        d.removeClass("sticked")
                    }
                })
            }
        },
    };
    a(document).ready(function () {
        b.initialize()
    });
    a(window).on("resize", function () {
        b.hoverDropdown();
        a(".top-search").slideUp();
        setTimeout(function () {
            b.navbarSticky()
        }, 500);
        a(".navbar-toggle").each(function () {
            a(".fa", this).removeClass("fa-times");
            a(".fa", this).addClass("fa-bars");
            a(this).removeClass("fixed")
        });
        a(".navbar-collapse").removeClass("in");
        a(".navbar-collapse").removeClass("on");
        a(".navbar-collapse").removeClass("bounceIn")
    })
}(jQuery));