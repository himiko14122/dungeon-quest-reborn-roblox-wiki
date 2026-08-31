import {
  BookOpen, Map, Swords, Skull, UserCircle, Wand2, ShieldCheck, BarChart3, Newspaper,
  Rocket, Layers, Zap, Crown,
  type LucideIcon,
} from 'lucide-react';

export interface StatConfig {
  val: string;
  labelKey: string;
}

export interface ModuleCardConfig {
  key: string;
  labelKey: string;
  titleKey: string;
  descKey: string;
  href: string;
  stats: StatConfig[];
  icon: LucideIcon;
  ctaKey?: string;
}

export interface GameFeatureConfig {
  titleKey: string;
  descKey: string;
  icon: LucideIcon;
}

export interface StartHereStepConfig {
  titleKey: string;
  descKey: string;
  href: string;
}

export interface HeroCtaConfig {
  labelKey: string;
  href: string;
  style: 'primary' | 'secondary';
}

export const HOME_CONFIG = {
  hero: {
    // DEGRADED: no official trailer — using hero image (new game Aug 2026, sparse video content)
    badgeKeys: [
      'home_hero_badge_visits',
      'home_hero_badge_favorites',
      'home_hero_badge_players',
      'home_hero_badge_launched',
      'home_hero_badge_updated',
    ],
    ctas: [
      { labelKey: 'home_hero_cta_guides', href: '/guides', style: 'primary' as const },
      { labelKey: 'home_hero_cta_dungeons', href: '/dungeons', style: 'secondary' as const },
      { labelKey: 'home_hero_cta_tierList', href: '/tier-list', style: 'secondary' as const },
    ],
  },

  moduleCards: [
    { key: 'guides', labelKey: 'home_module_guides', titleKey: 'home_module_guides_title', descKey: 'home_module_guides_desc', href: '/guides', stats: [{ val: '__guideCount', labelKey: 'home_module_guides_stat1' }, { val: '2 Classes', labelKey: 'home_module_guides_stat2' }], icon: BookOpen, ctaKey: 'home_module_guides_cta' },
    { key: 'dungeons', labelKey: 'home_module_dungeons', titleKey: 'home_module_dungeons_title', descKey: 'home_module_dungeons_desc', href: '/dungeons', stats: [{ val: '3', labelKey: 'home_module_dungeons_stat1' }, { val: 'Zones', labelKey: 'home_module_dungeons_stat2' }], icon: Map, ctaKey: 'home_module_dungeons_cta' },
    { key: 'weapons', labelKey: 'home_module_weapons', titleKey: 'home_module_weapons_title', descKey: 'home_module_weapons_desc', href: '/weapons', stats: [{ val: 'S-Tier', labelKey: 'home_module_weapons_stat1' }, { val: '60+', labelKey: 'home_module_weapons_stat2' }], icon: Swords, ctaKey: 'home_module_weapons_cta' },
    { key: 'bosses', labelKey: 'home_module_bosses', titleKey: 'home_module_bosses_title', descKey: 'home_module_bosses_desc', href: '/bosses', stats: [{ val: '3', labelKey: 'home_module_bosses_stat1' }, { val: 'Bosses', labelKey: 'home_module_bosses_stat2' }], icon: Skull, ctaKey: 'home_module_bosses_cta' },
    { key: 'classes', labelKey: 'home_module_classes', titleKey: 'home_module_classes_title', descKey: 'home_module_classes_desc', href: '/classes', stats: [{ val: 'Warrior', labelKey: 'home_module_classes_stat1' }, { val: 'Mage', labelKey: 'home_module_classes_stat2' }], icon: UserCircle, ctaKey: 'home_module_classes_cta' },
    { key: 'spells', labelKey: 'home_module_spells', titleKey: 'home_module_spells_title', descKey: 'home_module_spells_desc', href: '/spells', stats: [{ val: 'AoE', labelKey: 'home_module_spells_stat1' }, { val: 'Ground Slam', labelKey: 'home_module_spells_stat2' }], icon: Wand2, ctaKey: 'home_module_spells_cta' },
    { key: 'equipment', labelKey: 'home_module_equipment', titleKey: 'home_module_equipment_title', descKey: 'home_module_equipment_desc', href: '/equipment', stats: [{ val: 'Weapons', labelKey: 'home_module_equipment_stat1' }, { val: 'Armor+Helm', labelKey: 'home_module_equipment_stat2' }], icon: ShieldCheck, ctaKey: 'home_module_equipment_cta' },
    { key: 'tier-list', labelKey: 'home_module_tierList', titleKey: 'home_module_tierList_title', descKey: 'home_module_tierList_desc', href: '/tier-list', stats: [{ val: 'S+', labelKey: 'home_module_tierList_stat1' }, { val: 'Meta', labelKey: 'home_module_tierList_stat2' }], icon: BarChart3, ctaKey: 'home_module_tierList_cta' },
    { key: 'updates', labelKey: 'home_module_updates', titleKey: 'home_module_updates_title', descKey: 'home_module_updates_desc', href: '/updates', stats: [{ val: 'Live', labelKey: 'home_module_updates_stat1' }, { val: 'Aug 2026', labelKey: 'home_module_updates_stat2' }], icon: Newspaper, ctaKey: 'home_module_updates_cta' },
  ] as ModuleCardConfig[],

  gameFeatures: [
    { titleKey: 'home_feature_classes', descKey: 'home_feature_classes_desc', icon: Crown },
    { titleKey: 'home_feature_dungeons', descKey: 'home_feature_dungeons_desc', icon: Layers },
    { titleKey: 'home_feature_combat', descKey: 'home_feature_combat_desc', icon: Zap },
    { titleKey: 'home_feature_progression', descKey: 'home_feature_progression_desc', icon: Rocket },
  ] as GameFeatureConfig[],

  startHereSteps: [
    { titleKey: 'home_start_1_title', descKey: 'home_start_1_desc', href: '/guides' },
    { titleKey: 'home_start_2_title', descKey: 'home_start_2_desc', href: '/dungeons' },
    { titleKey: 'home_start_3_title', descKey: 'home_start_3_desc', href: '/classes' },
    { titleKey: 'home_start_4_title', descKey: 'home_start_4_desc', href: '/weapons' },
    { titleKey: 'home_start_5_title', descKey: 'home_start_5_desc', href: '/tier-list' },
  ] as StartHereStepConfig[],

  gameOverview: {
    infoItems: ['developer', 'platform', 'genre', 'visits', 'favorites', 'players', 'classes', 'zones'],
    cta: {
      guideLabelKey: 'home_about_cta',
      guideHref: '/guides',
      externalLabelKey: 'home_cta_roblox',
      externalLinkKey: 'roblox',
    },
  },

  faq: {
    keys: ['classes', 'leveling', 'gold', 'dungeons', 'bosses', 'gear', 'spells', 'multiplayer'],
  },

  bottomCta: {
    guideHref: '/guides',
    guideLabelKey: 'home_cta_guide',
    externalLinkKey: 'roblox',
    externalLabelKey: 'home_cta_roblox',
  },
};
