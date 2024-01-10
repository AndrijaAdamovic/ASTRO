#ifndef ASTRO_DIFFDRIVE__VISIBILITY_CONTROL_H_
#define ASTRO_DIFFDRIVE__VISIBILITY_CONTROL_H_

#if defined _WIN32 || defined __CYGWIN__
#ifdef __GNUC__
#define ASTRO_DIFFDRIVE_EXPORT __attribute__((dllexport))
#define ASTRO_DIFFDRIVE_IMPORT __attribute__((dllimport))
#else
#define ASTRO_DIFFDRIVE_EXPORT __declspec(dllexport)
#define ASTRO_DIFFDRIVE_IMPORT __declspec(dllimport)
#endif
#ifdef ASTRO_DIFFDRIVE_BUILDING_DLL
#define ASTRO_DIFFDRIVE_PUBLIC ASTRO_DIFFDRIVE_EXPORT
#else
#define ASTRO_DIFFDRIVE_PUBLIC ASTRO_DIFFDRIVE_IMPORT
#endif
#define ASTRO_DIFFDRIVE_PUBLIC_TYPE ASTRO_DIFFDRIVE_PUBLIC
#define ASTRO_DIFFDRIVE_LOCAL
#else
#define ASTRO_DIFFDRIVE_EXPORT __attribute__((visibility("default")))
#define ASTRO_DIFFDRIVE_IMPORT
#if __GNUC__ >= 4
#define ASTRO_DIFFDRIVE_PUBLIC __attribute__((visibility("default")))
#define ASTRO_DIFFDRIVE_LOCAL __attribute__((visibility("hidden")))
#else
#define ASTRO_DIFFDRIVE_PUBLIC
#define ASTRO_DIFFDRIVE_LOCAL
#endif
#define ASTRO_DIFFDRIVE_PUBLIC_TYPE
#endif

#endif  // ASTRO_DIFFDRIVE__VISIBILITY_CONTROL_H_