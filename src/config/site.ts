import { routing, type Locale } from '@/i18n/routing';

export const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://dungeon-quest-reborn-roblox.wiki';
export const SITE_NAME = 'Dungeon Quest Reborn Wiki';
export const HERO_IMAGE = '/images/hero.webp';
export const LOGO_IMAGE = '/logo.svg';
export const TWITTER_HANDLE = '';
export const GA_TRACKING_ID = 'G-TG3RRG4Q9M';
export const SLUG_PREFIX = 'Dungeon-Quest-Reborn-';

export const EXTERNAL_LINKS = {
  roblox: 'https://www.roblox.com/games/77649408247578/Dungeon-Quest-Reborn',
  discord: '',
  youtube: '',
  reddit: '',
  twitter: '',
  website: '',
} as const;

export function absoluteUrl(path = '/') {
  const normalized = path.startsWith('/') ? path : `/${path}`;
  return `${SITE_URL}${normalized}`;
}

export function localizedPath(locale: Locale | string, path = '/') {
  const normalized = path === '' ? '/' : path.startsWith('/') ? path : `/${path}`;
  if (locale === routing.defaultLocale) {
    return normalized === '/' ? '/' : normalized;
  }
  return normalized === '/' ? `/${locale}` : `/${locale}${normalized}`;
}
