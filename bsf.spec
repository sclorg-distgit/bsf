%{?scl:%scl_package bsf}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}bsf
Epoch:          0
Version:        2.4.0
Release:        26.1%{?dist}
Summary:        Bean Scripting Framework
License:        ASL 2.0
URL:            http://commons.apache.org/bsf/
BuildArch:      noarch

Source0:        http://apache.mirror.anlx.net//commons/%{pkg_name}/source/%{pkg_name}-src-%{version}.tar.gz
Source1:        %{pkg_name}-pom.xml

Patch0:         build-file.patch
Patch1:         build.properties.patch

BuildRequires:  %{?scl_prefix}javapackages-local
BuildRequires:  %{?scl_prefix}ant
BuildRequires:  %{?scl_prefix}apache-parent
BuildRequires:  %{?scl_prefix}xalan-j2
BuildRequires:  %{?scl_prefix}rhino
BuildRequires:  %{?scl_prefix}apache-commons-logging

%description
Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications, and access to Java
objects and methods from scripting languages. BSF allows one to write
JSPs in languages other than Java while providing access to the Java
class library. In addition, BSF permits any Java application to be
implemented in part (or dynamically extended) by a language that is
embedded within it. This is achieved by providing an API that permits
calling scripting language engines from within Java, as well as an
object registry that exposes Java objects to these scripting language
engines.

BSF supports several scripting languages currently:
* Javascript (using Rhino ECMAScript, from the Mozilla project)
* Python (using either Jython or JPython)
* Tcl (using Jacl)
* NetRexx (an extension of the IBM REXX scripting language in Java)
* XSLT Stylesheets (as a component of Apache XML project's Xalan and
Xerces)

In addition, the following languages are supported with their own BSF
engines:
* Java (using BeanShell, from the BeanShell project)
* JRuby
* JudoScript

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1
%patch1 -p1
find -name \*.jar -delete

%mvn_file : %{pkg_name}
%mvn_alias : org.apache.bsf:

%build
export CLASSPATH=$(build-classpath apache-commons-logging rhino xalan-j2)
ant jar javadocs

%mvn_artifact %{SOURCE1} build/lib/%{pkg_name}.jar

%install
%mvn_install -J build/javadocs

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc AUTHORS.txt CHANGES.txt README.txt TODO.txt RELEASE-NOTE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 0:2.4.0-26.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Michael Simacek <msimacek@redhat.com> - 0:2.4.0-26
- Add missing BR apache-parent

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 14 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.0-24
- Cleanup package

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:2.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.0-22
- Add build-requires on javapackages-local

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.0-20
- Disable javadoc doclint

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.0-18
- Use .mfiles generated during build
- Update to current packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Tomas Radej <tradej@redhat.com> - 0:2.4.0-15
- Fixed URL of Source0

* Tue Nov 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.4.0-14
- Remove unneeded BR: jython

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.0-12
- Drop jsp/servlet api dependencies, leftovers from the past.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.4.0-10
- Fixes according to latest guidelines
- Fix maven depmap

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 21 2010 Orion Poplawski <orion@cora.nwra.com> - 0:2.4.0-8
- Build against rhino for JavaScript support

* Mon Jun 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.4.0-7
- Added pom file to enable maven dependency resolution
- Fix Source0 URL
- Fix Group designation

* Mon Jun  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.4.0-6
- Fix BR after jakarta-commons rename

* Wed Apr 7 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.0-5
- Drop gcj support.
- Build against servlet and jsp apis from tomcat6.

* Mon Jan 11 2010 Andrew Overholt <overholt@redhat.com> 2.4.0-4
- Fix License (ASL 2.0 and not 1.1) (rhbz#554465).

* Mon Sep 14 2009 Christoph Höger <choeger@cs.tu-berlin.de> - 0:2.4.0-3
- Fix typo in Requires

* Wed Sep 09 2009 Christoph Höger <choeger@cs.tu-berlin.de> - 0:2.4.0-1
- New Upstream release: 2.4.0
- Add jython build dependency to include bsf-jython engine

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:2.3.0-13
- drop repotag
- fix license

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:2.3.0-12jpp.2
- Autorebuild for GCC 4.3

* Wed Mar 07 2007 Permaine Cheung <pcheung@redhat.com> 0:2.3.0-11jpp.2
- Update spec file as per Fedora guidelines

* Thu Aug 03 2006 Deepak Bhole <dbhole@redhat.com> 0:2.3.0-11jpp.1
- Added missing requirements.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> 0:2.3.0-10jpp_2fc
- Rebuilt

* Fri Jul 21 2006 Deepak Bhole <dbhole@redhat.com> 0:2.3.0-10jpp_2fc
- Removing vendor and distribution tags.

* Thu Jul 20 2006 Deepak Bhole <dbhole@redhat.com> 0:2.3.0-10jpp_1fc
- Added conditional native compilation.
- From gbenson@redhat:
-   Build without Jython or Rhino for now.
-   Build with servletapi5.
-   Avoid Sun-specific classes.

* Wed Apr 26 2006 Fernando Nasser <fnasser@redhat.com>  0:2.3.0-9jpp
- First JPP 1.7 build

* Wed Nov 3 2004 Nicolas Mailhot <nim@jpackage.org>  0:2.3.0-8jpp
- Clean up specfile a bit

* Fri Aug 20 2004 Ralph Apel <r.apel at r-apel.de> 0:2.3.0-7jpp
- Build with ant-1.6.2

* Thu Oct 09 2003 David Walluck <david@anti-microsoft.org> 0:2.3.0-6jpp
- add javadoc symlinks
- change Apache Software License to Apache License

* Tue Aug 26 2003 David Walluck <david@anti-microsoft.org> 0:2.3.0-5jpp
- remove all Requires

* Fri Apr 12 2003 David Walluck <david@anti-microsoft.org> 0:2.3.0-4jpp
- fix strange permissions

* Fri Apr 11 2003 David Walluck <david@anti-microsoft.org> 0:2.3.0-3jpp
- rebuild for jpackage 1.5

* Wed Jan 22 2003 David Walluck <david@anti-microsoft.org> 2.3.0-2jpp
- Requires/BuildRequires: xalan-j2
- update %%description

* Mon Jan 13 2003 David Walluck <david@anti-microsoft.org> 2.3.0-1jpp
- version 2.3.0 (first jakarta release)

* Tue May 07 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2-5jpp
- vendor, distribution, group tags
- versioned dir for javadoc
- section macro

* Sat Dec 1 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2-4jpp
- javadoc in javadoc package

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 2.2-3jpp
- removed packager tag
- new jpp extension
- fixed url

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2-2jpp
- first unified release
- used original tarball
- s/jPackage/JPackage

* Thu Aug 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2-1jpp
- first Mandrake release
