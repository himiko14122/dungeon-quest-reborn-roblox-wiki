// Game-specific data for Dungeon Quest Reborn
// Color maps, entity structures, and tier utilities

/* ──────────────── Color Maps ──────────────── */
export const TIER_COLOR_MAP: Record<string, string> = {
  S: 'var(--color-tier-s)',
  A: 'var(--color-tier-a)',
  B: 'var(--color-tier-b)',
  C: 'var(--color-tier-c)',
};
export const TIER_COLOR_DEFAULT = 'var(--color-tier-c)';

export function tierColor(tier: string): string {
  return TIER_COLOR_MAP[tier] ?? TIER_COLOR_DEFAULT;
}

export const RARITY_COLOR_MAP: Record<string, string> = {
  Legendary: 'var(--color-rarity-legendary)',
  Epic: 'var(--color-rarity-epic)',
  Rare: 'var(--color-rarity-rare)',
  Common: 'var(--color-rarity-common)',
};

/* ──────────────── Weapons (homepage Table 1) ──────────────── */
export interface WeaponEntry {
  id: string;
  nameKey: string;
  typeKey: string;
  sourceKey: string;
  dpsKey: string;
  tier: string;
  rarity: string;
}

export const WEAPONS: WeaponEntry[] = [
  { id: 'crystal-skull-sword', nameKey: 'weapon_0_name', typeKey: 'weapon_0_type', sourceKey: 'weapon_0_source', dpsKey: 'weapon_0_dps', tier: 'S', rarity: 'Legendary' },
  { id: 'snowblade', nameKey: 'weapon_1_name', typeKey: 'weapon_1_type', sourceKey: 'weapon_1_source', dpsKey: 'weapon_1_dps', tier: 'S', rarity: 'Legendary' },
  { id: 'soul-reaper', nameKey: 'weapon_2_name', typeKey: 'weapon_2_type', sourceKey: 'weapon_2_source', dpsKey: 'weapon_2_dps', tier: 'A', rarity: 'Epic' },
  { id: 'pirates-sword', nameKey: 'weapon_3_name', typeKey: 'weapon_3_type', sourceKey: 'weapon_3_source', dpsKey: 'weapon_3_dps', tier: 'A', rarity: 'Epic' },
  { id: 'frozen-greatsword', nameKey: 'weapon_4_name', typeKey: 'weapon_4_type', sourceKey: 'weapon_4_source', dpsKey: 'weapon_4_dps', tier: 'B', rarity: 'Rare' },
  { id: 'sands-of-time', nameKey: 'weapon_5_name', typeKey: 'weapon_5_type', sourceKey: 'weapon_5_source', dpsKey: 'weapon_5_dps', tier: 'B', rarity: 'Rare' },
  { id: 'steel-sword', nameKey: 'weapon_6_name', typeKey: 'weapon_6_type', sourceKey: 'weapon_6_source', dpsKey: 'weapon_6_dps', tier: 'C', rarity: 'Common' },
  { id: 'wooden-sword', nameKey: 'weapon_7_name', typeKey: 'weapon_7_type', sourceKey: 'weapon_7_source', dpsKey: 'weapon_7_dps', tier: 'C', rarity: 'Common' },
];

/* ──────────────── Spells (homepage Cards 1) ──────────────── */
export interface SpellEntry {
  id: string;
  nameKey: string;
  classKey: string;
  effectKey: string;
  bestKey: string;
  tier: string;
}

export const SPELLS: SpellEntry[] = [
  { id: 'ground-slam', nameKey: 'spell_0_name', classKey: 'spell_0_class', effectKey: 'spell_0_effect', bestKey: 'spell_0_best', tier: 'S' },
  { id: 'ice-storm', nameKey: 'spell_1_name', classKey: 'spell_1_class', effectKey: 'spell_1_effect', bestKey: 'spell_1_best', tier: 'S' },
  { id: 'fire-surge', nameKey: 'spell_2_name', classKey: 'spell_2_class', effectKey: 'spell_2_effect', bestKey: 'spell_2_best', tier: 'A' },
  { id: 'lightning-strike', nameKey: 'spell_3_name', classKey: 'spell_3_class', effectKey: 'spell_3_effect', bestKey: 'spell_3_best', tier: 'A' },
  { id: 'healing-wave', nameKey: 'spell_4_name', classKey: 'spell_4_class', effectKey: 'spell_4_effect', bestKey: 'spell_4_best', tier: 'B' },
  { id: 'ember', nameKey: 'spell_5_name', classKey: 'spell_5_class', effectKey: 'spell_5_effect', bestKey: 'spell_5_best', tier: 'B' },
];

/* ──────────────── Dungeons (homepage Table 2) ──────────────── */
export interface DungeonEntry {
  id: string;
  nameKey: string;
  levelKey: string;
  bossKey: string;
  rewardKey: string;
  tier: string;
}

export const DUNGEONS: DungeonEntry[] = [
  { id: 'pirate-island', nameKey: 'dungeon_0_name', levelKey: 'dungeon_0_level', bossKey: 'dungeon_0_boss', rewardKey: 'dungeon_0_reward', tier: 'S' },
  { id: 'winter-outpost', nameKey: 'dungeon_1_name', levelKey: 'dungeon_1_level', bossKey: 'dungeon_1_boss', rewardKey: 'dungeon_1_reward', tier: 'A' },
  { id: 'desert-temple', nameKey: 'dungeon_2_name', levelKey: 'dungeon_2_level', bossKey: 'dungeon_2_boss', rewardKey: 'dungeon_2_reward', tier: 'B' },
];

/* ──────────────── Classes (homepage Cards 2) ──────────────── */
export interface ClassEntry {
  id: string;
  nameKey: string;
  roleKey: string;
  weaponKey: string;
  spellKey: string;
  tier: string;
}

export const CLASSES: ClassEntry[] = [
  { id: 'warrior', nameKey: 'class_0_name', roleKey: 'class_0_role', weaponKey: 'class_0_weapon', spellKey: 'class_0_spell', tier: 'S' },
  { id: 'mage', nameKey: 'class_1_name', roleKey: 'class_1_role', weaponKey: 'class_1_weapon', spellKey: 'class_1_spell', tier: 'S' },
];

/* ──────────────── Bosses (data for category page) ──────────────── */
export interface BossEntry {
  id: string;
  nameKey: string;
  dungeonKey: string;
  attackKey: string;
  lootKey: string;
  tier: string;
}

export const BOSSES: BossEntry[] = [
  { id: 'sand-giant', nameKey: 'boss_0_name', dungeonKey: 'boss_0_dungeon', attackKey: 'boss_0_attack', lootKey: 'boss_0_loot', tier: 'B' },
  { id: 'frost-wizard', nameKey: 'boss_1_name', dungeonKey: 'boss_1_dungeon', attackKey: 'boss_1_attack', lootKey: 'boss_1_loot', tier: 'A' },
  { id: 'captain-blaze', nameKey: 'boss_2_name', dungeonKey: 'boss_2_dungeon', attackKey: 'boss_2_attack', lootKey: 'boss_2_loot', tier: 'S' },
];

/* ──────────────── Sidebar Codes ──────────────── */
export interface SidebarCode {
  code: string;
  reward: string;
}

// Dungeon Quest Reborn has no known active redemption codes (research verified).
// Per the two-state contract, we include only a single placeholder entry.
export const SIDEBAR_CODES: SidebarCode[] = [
  { code: 'None', reward: 'No active codes yet. Check back soon!' },
];

/* ──────────────── Footer Data ──────────────── */
export const FOOTER_DATA = {
  officialDiscordUrl: '',
  officialYoutubeUrl: '',
  communityTool: { label: '', href: '' },
} as const;
