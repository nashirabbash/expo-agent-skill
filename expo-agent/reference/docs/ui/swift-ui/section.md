---
title: "Section"
description: "A SwiftUI Section component for grouping content within lists and forms."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/section.md"
scraped_at: "2026-07-15T08:59:26.225974"
---

---
title: Section
description: A SwiftUI Section component for grouping content within lists and forms.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Section

A SwiftUI Section component for grouping content within lists and forms.
iOS, tvOS, Included in Expo Go

Expo UI Section matches the official SwiftUI [Section API](https://developer.apple.com/documentation/swiftui/section) and is used to group related content within [`List`](/versions/latest/sdk/ui/swift-ui/list.md), [`Form`](/versions/latest/sdk/ui/swift-ui/form.md) or [`Picker`](/versions/latest/sdk/ui/swift-ui/picker.md) components.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic section with title

Use the `title` prop for simple sections with a text header.

```tsx
import { Host, List, Section, Text } from '@expo/ui/swift-ui';

export default function BasicSectionExample() {
  return (
    <Host style={{ flex: 1 }}>
      <List>
        <Section title="Settings">
          <Text>General</Text>
          <Text>Privacy</Text>
          <Text>Notifications</Text>
        </Section>
      </List>
    </Host>
  );
}
```

### Section with custom header and footer

Use the `header` and `footer` props for custom views. These props are only used when `title` is not provided.

```tsx
import { Host, List, Section, Toggle, Text, HStack, Image } from '@expo/ui/swift-ui';
import { useState } from 'react';

export default function CustomHeaderFooterExample() {
  const [locationEnabled, setLocationEnabled] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <List>
        <Section
          header={
            <HStack>
              <Image systemName="location.fill" color="blue" size={16} />
              <Text>Location Services</Text>
            </HStack>
          }
          footer={
            <Text>
              Enabling location services allows the app to provide personalized recommendations.
            </Text>
          }>
          <Toggle
            label="Enable Location"
            isOn={locationEnabled}
            onIsOnChange={setLocationEnabled}
          />
        </Section>
      </List>
    </Host>
  );
}
```

### Collapsible section

Use the `isExpanded` prop to control whether the section is expanded or collapsed. When provided, the section becomes collapsible. Use `onIsExpandedChange` to handle state changes.

> **Note:** Collapsible sections require iOS 17+ and tvOS 17+, and the list must use the `sidebar` style. Footer is not supported for collapsible sections.

```tsx
import { useState } from 'react';
import { Host, List, Section, Text } from '@expo/ui/swift-ui';
import { listStyle } from '@expo/ui/swift-ui/modifiers';

export default function CollapsibleSectionExample() {
  const [favoritesExpanded, setFavoritesExpanded] = useState(false);
  const [recentsExpanded, setRecentsExpanded] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <List modifiers={[listStyle('sidebar')]}>
        <Section
          title="Favorites"
          isExpanded={favoritesExpanded}
          onIsExpandedChange={setFavoritesExpanded}>
          <Text>Home</Text>
          <Text>Work</Text>
          <Text>Gym</Text>
        </Section>
        <Section
          title="Recents"
          isExpanded={recentsExpanded}
          onIsExpandedChange={setRecentsExpanded}>
          <Text>Coffee Shop</Text>
          <Text>Library</Text>
          <Text>Park</Text>
        </Section>
      </List>
    </Host>
  );
}
```

### Multiple sections in a form

Sections work within `Form` components to organize form controls into logical groups.

```tsx
import { useState } from 'react';
import { Host, Form, Section, Toggle, Picker, Text, Button } from '@expo/ui/swift-ui';
import { pickerStyle, tag } from '@expo/ui/swift-ui/modifiers';

export default function FormSectionsExample() {
  const [darkMode, setDarkMode] = useState(false);
  const [notifications, setNotifications] = useState(true);
  const [language, setLanguage] = useState(0);
  const languages = ['English', 'Spanish', 'French', 'German'];

  return (
    <Host style={{ flex: 1 }}>
      <Form>
        <Section title="Appearance">
          <Toggle label="Dark Mode" isOn={darkMode} onIsOnChange={setDarkMode} />
          <Picker
            label="Language"
            selection={language}
            onSelectionChange={setLanguage}
            modifiers={[pickerStyle('menu')]}>
            {languages.map((lang, index) => (
              <Text key={index} modifiers={[tag(index)]}>
                {lang}
              </Text>
            ))}
          </Picker>
        </Section>
        <Section title="Notifications">
          <Toggle label="Push Notifications" isOn={notifications} onIsOnChange={setNotifications} />
        </Section>
        <Section title="Account">
          <Button label="Sign Out" role="destructive" onPress={() => alert('Signed out')} />
        </Section>
      </Form>
    </Host>
  );
}
```

## API

```tsx
import { Section } from '@expo/ui/swift-ui';
```

## Component

### `Section`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SectionProps](#sectionprops)\>

Section component uses the native [Section](https://developer.apple.com/documentation/swiftui/section) component.

SectionProps

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content of the section.

### `footer`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Sets a custom footer for the section.

### `header`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Sets a custom header for the section.

### `isExpanded`

Supported platforms: iOS 17.0+, tvOS 17.0+.

Optional • Type: `boolean`

Controls whether the section is expanded or collapsed. When provided, the section becomes collapsible.

> **Note**: Available only when the list style is set to `sidebar`.

### `onIsExpandedChange`

Supported platforms: iOS 17.0+, tvOS 17.0+.

Optional • Type: `(isExpanded: boolean) => void`

Callback triggered when the section's expanded state changes.

### `title`

Supported platforms: iOS, tvOS.

Optional • Type: `string`

The title of the section.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
