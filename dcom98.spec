# This spec file is released under the GNU General Public License version 2.0
# (http://www.gnu.org/licenses/gpl.txt).
#
# NOTE: Releasing this spec file under the GPL does not alter the licensing of
# DCOM98 itself. Satisfying the terms of DCOM98's license remains the user's
# responsibility.

%define	ver	1.3
%define	rel	3
%define _wine_cdrive	%{_datadir}/wine
%define _wine_system	%{_wine_cdrive}/windows/system

Summary:	Package of DLLs supporting Microsoft's DCOM framework.
Name:		dcom98
Version:	%ver
Release:	%rel
Vendor:		Microsoft
Source0:	http://download.microsoft.com/msdownload/dcom/98/x86/en/%{name}.exe
Requires:	wine, wine-utils
BuildRequires:	wine, cabextract
Group:		System/Libraries
######		Unknown group!
License:	Distributable
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Url:		http://www.microsoft.com/com/tech/DCOM.asp
ExclusiveArch:	%{ix86}
Obsoletes:	dcom


%description
The Distributed Component Object Model (DCOM) is a protocol that
enables software components to communicate directly over a network in
a reliable, secure, and efficient manner. Previously called "Network
OLE," DCOM is designed for use across multiple network transports,
including Internet protocols such as HTTP. DCOM is based on the Open
Software Foundation's DCE-RPC spec and will work with both Java
applets and ActiveX� components through its use of the Component
Object Model (COM). Follow the links below to learn more about DCOM.

%prep
/usr/bin/cabextract -L $RPM_SOURCE_DIR/dcom98.exe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_wine_system}
install -d $RPM_BUILD_ROOT/%{_wine_cdrive}/inf/
mv advpack.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv asycfilt.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv comcat.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv compobj.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv dcom98.inf $RPM_BUILD_ROOT/%{_wine_cdrive}/inf/
mv dllhost.exe $RPM_BUILD_ROOT/%{_wine_system}/
mv imagehlp.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv iprop.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv ole2.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv ole32.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv oleaut32.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv olecnv32.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv olepro32.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv olethk32.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcltc1.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcltc5.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcltccm.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpclts5.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcltscm.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcmqcl.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcmqsvr.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcns4.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcrt4.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv rpcss.exe $RPM_BUILD_ROOT/%{_wine_system}/
mv secur32.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv stdole2.tlb $RPM_BUILD_ROOT/%{_wine_system}/
mv stdole32.tlb $RPM_BUILD_ROOT/%{_wine_system}/
mv storage.dll $RPM_BUILD_ROOT/%{_wine_system}/
mv w95inf16.dll $RPM_BUILD_ROOT/%{_wine_system}/w95inf16.dll
mv w95inf32.dll $RPM_BUILD_ROOT/%{_wine_system}/w95inf32.dll

rm -f eula98.txt
rm -f relnt98.txt
rm -f install.exe

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_wine_system}/advpack.dll
%{_wine_system}/asycfilt.dll
%{_wine_system}/comcat.dll
%{_wine_system}/compobj.dll
%{_wine_cdrive}/inf/dcom98.inf
%{_wine_system}/dllhost.exe
%{_wine_system}/imagehlp.dll
%{_wine_system}/iprop.dll
%{_wine_system}/ole2.dll
%{_wine_system}/ole32.dll
%{_wine_system}/oleaut32.dll
%{_wine_system}/olecnv32.dll
%{_wine_system}/olepro32.dll
%{_wine_system}/olethk32.dll
%{_wine_system}/rpcltc1.dll
%{_wine_system}/rpcltc5.dll
%{_wine_system}/rpcltccm.dll
%{_wine_system}/rpclts5.dll
%{_wine_system}/rpcltscm.dll
%{_wine_system}/rpcmqcl.dll
%{_wine_system}/rpcmqsvr.dll
%{_wine_system}/rpcns4.dll
%{_wine_system}/rpcrt4.dll
%{_wine_system}/rpcss.exe
%{_wine_system}/secur32.dll
%{_wine_system}/stdole2.tlb
%{_wine_system}/stdole32.tlb
%{_wine_system}/storage.dll
%{_wine_system}/w95inf16.dll
%{_wine_system}/w95inf32.dll