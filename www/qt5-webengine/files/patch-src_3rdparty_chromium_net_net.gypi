--- src/3rdparty/chromium/net/net.gypi.orig	2017-04-19 19:48:59 UTC
+++ src/3rdparty/chromium/net/net.gypi
@@ -435,8 +435,8 @@
       'android/network_library.h',
       'android/traffic_stats.cc',
       'android/traffic_stats.h',
-      'base/address_tracker_linux.cc',
-      'base/address_tracker_linux.h',
+      # 'base/address_tracker_linux.cc',
+      # 'base/address_tracker_linux.h',
       'base/backoff_entry.cc',
       'base/backoff_entry.h',
       'base/backoff_entry_serializer.cc',
@@ -497,8 +497,8 @@
       'base/network_change_notifier.cc',
       'base/network_change_notifier.h',
       'base/network_change_notifier_factory.h',
-      'base/network_change_notifier_linux.cc',
-      'base/network_change_notifier_linux.h',
+      # 'base/network_change_notifier_linux.cc',
+      # 'base/network_change_notifier_linux.h',
       'base/network_change_notifier_mac.cc',
       'base/network_change_notifier_mac.h',
       'base/network_change_notifier_win.cc',
@@ -509,7 +509,7 @@
       'base/network_delegate.h',
       'base/network_delegate_impl.cc',
       'base/network_delegate_impl.h',
-      'base/network_interfaces_linux.cc',
+      # 'base/network_interfaces_linux.cc',
       'base/network_interfaces_mac.cc',
       'base/network_interfaces_win.cc',
       'base/network_quality_estimator.cc',
